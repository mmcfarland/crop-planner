from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Context, Template
from functools import wraps

from planner.forms import LoginForm
from planner.models import GardenSite, SiteUser

def route(**kwargs):
    def routed(request, **kwargs2):
        req_method = kwargs[request.method]
        print req_method.__name__
        return req_method(request, **kwargs2)
    return routed

def site_request(view_fn):
    @wraps(view_fn)
    def wrapper(request, garden_site_id, *args, **kwargs):
        request.garden_site = get_object_or_404(GardenSite, pk=garden_site_id)
        return view_fn(request, *args, **kwargs)

    return wrapper

def get_login(req):
    login = LoginForm()
    context = {'form': login}
    return render_to_response('login.html', context, RequestContext(req))

def auth(req):
    # Kill any existing session
    logout(req)

    login_form = LoginForm(req.POST)
    if login_form.is_valid():
        u = login_form.cleaned_data['username']
        p = login_form.cleaned_data['password']
        user = authenticate(username=u, password=p)

        if user is not None:
            if user.is_active:
                # Use session to keep garden site around, which will scope resources
                login(req, user)
                req.session['garden_site'] = SiteUser.query.by(user).site
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/not-active/')
        else:
            login_form.add_form_error("Incorrect username or password")

    return render_to_response('login.html', {'form':login_form }, RequestContext(req))

@login_required()
def home(req):
    c = {
        'garden': req.session['garden_site']
    }
    return render_to_response('home.html', c, RequestContext(req))
