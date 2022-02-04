from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'priority', 'is_completed', 'until', 'user', )
    list_display_links = ('pk', 'title', )
    list_filter = ('is_completed', 'until', 'user', 'created_at', )
    list_editable = ('is_completed', 'priority')
    fields = ('title', 'description', 'until', 'is_completed', 'user', 'priority', 'created_at', )
    ordering = ('is_completed', '-priority', 'title', )
    readonly_fields = ('user', 'created_at', )


admin.site.register(Task, TaskAdmin)
