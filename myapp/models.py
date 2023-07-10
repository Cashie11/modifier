from django.db import models

class UserData(models.Model):
    code = models.CharField(max_length=10, unique=True)
    data = models.TextField()


# Create your models here.
