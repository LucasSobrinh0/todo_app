from django.db import models

class Todo(models.Model):
    task_title = models.CharField(max_length=100, verbose_name="Title of the Task")
    entry = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.task_title
