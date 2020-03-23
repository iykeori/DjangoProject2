from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Maincat(models.Model):
    category = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category

    # def snippet(self):
    #     return self.body[:50]+'...'

