from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Context, Template

from django.contrib.auth.models import User
from planner.forms import LoginForm

def route(**kwargs):
    def routed(request, **kwargs2):
        req_method = kwargs[request.method]
        print req_method.__name__
        return req_method(request, **kwargs2)
    return routed

def get_login(req):
    login = LoginForm()
    context = {'form': login}
    return render_to_response('login.html', context, RequestContext(req))

def auth(req):
    login = LoginForm(req.POST)
    if login.is_valid():

        p = login.cleaned_data['password']
        user = authenticate(username=login.cleaned_data['username'], password=p)

        if user is not None:
            if user.is_active:
                pass
            else:
                pass
        else:
            print 'non'
            login.add_form_error("Incorrect username or password")
            return render_to_response('login.html', {'form':login }, RequestContext(req))