from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

from accounts.forms import UserRegistrationForm, UserLoginForm


class UserRegister(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

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
