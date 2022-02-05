from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import re


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(
        label=_("E-mail"),
        strip=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'new-email'}),
        help_text='Enter valid E-mail',
    )

    class Meta:
        model = User
        fields = ("username", "email", )

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_.%-+]{,63}@[a-zA-Z0-9]{1}[a-zA-Z0-9.-]{0,}\.[a-z|A-Z]{2,}]{,254}$'
        if not re.match(pattern, email):
            raise ValidationError("Not valid e-mail address")
        return email
    