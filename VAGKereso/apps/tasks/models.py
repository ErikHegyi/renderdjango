from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):
    # Task name
    name = models.CharField(max_length=100)

    # Task answer
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassProfile(AbstractUser):
    # The completed tasks
    completed_tasks = models.ManyToManyField(Task)

    def __str__(self):
        string = str(self.username)
        return string[0] + ". " + string[1]

    def add_task(self, task: Task):
        self.completed_tasks.add(task)

