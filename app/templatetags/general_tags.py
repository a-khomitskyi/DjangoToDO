from django import template
from app.models import Task


register = template.Library()


@register.inclusion_tag('app/list_task.html')
def get_tasks():
    task_list = Task.objects.all()
    return {'tasks': task_list}
