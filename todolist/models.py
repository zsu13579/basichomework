from django.db import models

# Create your models here.

class TodoList(models.Model):
    item = models.TextField(max_length=500)
    intime = models.DateTimeField(default='2016-03-01 0:0:0')
    deletetag = models.IntegerField(default=0)

    class Meta:
        db_table = 'todolist'
        ordering = ['deletetag']
