from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import Task
from .forms import UserRegistrationForm


class HomeView(LoginRequiredMixin, ListView):
    context_object_name = 'tasks'
    template_name = 'app/index.html'
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['cnt'] = context['tasks'].count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'task'
    template_name = 'app/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs['pk'])


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('title', 'description', 'priority', 'until', )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'description', 'priority', 'until', )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'app/task_delete.html'
    success_url = reverse_lazy('home')


class UserRegister(FormView):
    template_name = 'app/registration.html'
    form_class = UserRegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)


def action(request, pk):
    """Method makes a task completed or uncompleted"""
    # Doesn't work...
    # Task.objects.filter(pk=pk).update(is_completed=not F('is_completed'))
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse_lazy('home'))


class UserLoginView(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


"""
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return reverse_lazy('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/registration.html', {'form': form})
"""