from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import UserRegistrationForm, UserLoginForm, UserPasswordResetForm
from os import getenv


class UserRegister(SuccessMessageMixin, FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    success_message = 'You have been creating an account. Good luck!'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(UserRegister, self).get(request, *args, **kwargs)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    from_email = getenv('EMAIL_HOST_USER')
    form_class = UserPasswordResetForm
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


class UserPasswordResetDone(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    success_message = 'Your password has been set. You may login right now!'
