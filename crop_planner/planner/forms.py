from django import forms
from django.forms.util import ErrorDict
from django.forms.forms import NON_FIELD_ERRORS


class BaseForm(forms.Form):
    def add_form_error(self, message):
        if not self._errors:
            self._errors = ErrorDict()
        if not NON_FIELD_ERRORS in self._errors:
            self._errors[NON_FIELD_ERRORS] = self.error_class()
        self._errors[NON_FIELD_ERRORS].append(message)


class LoginForm(BaseForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
