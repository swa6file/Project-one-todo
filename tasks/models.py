from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Task(models.Model):
     title =models.CharField(max_length=50)
     description = models.CharField(max_length=250)
     completed = models.BooleanField(default=False)
     person = models.ForeignKey(User,verbose_name="пользователь",on_delete=models.CASCADE,related_name='persons')

     def __str__(self):
          return self.title


      # def get_absolute_url(self):
     #      return reverse('category', kwargs={'cat_slug': self.slug})

     class Meta:
          verbose_name = "Задача пользователя"
          verbose_name_plural= "Задачи пользователей"