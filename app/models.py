from django.db import models
from django.contrib.auth.models import User


CHOICES = (
        (1, 'Low'),
        (2, 'Middle'),
        (3, 'High'),
    )


class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    until = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    priority = models.IntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('is_completed', '-priority', 'title', )
