from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django import forms
import re


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    email = forms.CharField(
        label=_("E-mail"),
        strip=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'on'}),
        help_text='Your valid E-mail address',
    )

    class Meta:
        model = User
        fields = ("username", "email", )
        widgets = {'class': 'form-control'}

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-]{0,}\.[a-z|A-Z]{2,}]{,254}$'
        if not re.match(pattern, email):
            raise ValidationError("Not valid e-mail address")
        return email


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
