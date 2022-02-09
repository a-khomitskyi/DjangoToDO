from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Task
from .forms import TaskCreateForm


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'app/index.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed'] = Task.objects.filter(user=self.request.user).filter(is_completed=False).count() or 0

        return context

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskSearchView(HomeView):
    template_name = 'app/search_task.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context

    def get_queryset(self):
        search_input = self.request.GET.get('search')
        return Task.objects.filter(user=self.request.user).filter(title__icontains=search_input) | Task.objects.filter(
            user=self.request.user).filter(description__icontains=search_input)


class TaskDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    context_object_name = 'task'
    template_name = 'app/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs['pk'])

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class TaskDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'app/task_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


def action(request, pk):
    """Method makes a task completed or uncompleted"""
    # Doesn't work...
    # Task.objects.filter(pk=pk).update(is_completed=not F('is_completed'))
    task = Task.objects.get(pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse_lazy('home'))


def drop_all_completed(request):
    """Method has to drop all the completed tasks by user"""
    if request.method == 'POST':
        to_delete = Task.objects.filter(user=request.user).filter(is_completed=True)
        if to_delete:
            to_delete.delete()
        return redirect(reverse_lazy('home'))
    to_delete = Task.objects.filter(user=request.user).filter(is_completed=True).count()
    task = {'title': f'{to_delete} tasks'}
    return render(request, 'app/task_delete.html', {'task': task})
