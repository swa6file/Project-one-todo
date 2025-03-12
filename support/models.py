from django.contrib.auth.models import User
from django.db import models

class Support(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    solved = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.title



# Create your models here.
