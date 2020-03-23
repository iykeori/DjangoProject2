from django.db import models
#from django.contrib.auth.models import User
from maincat.models import Maincat

# Create your models here.
class Product(models.Model):
    item_title = models.CharField(max_length=100)
    category = models.ForeignKey(Maincat, default=None) #category
    description = models.TextField()
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #author = models.ForeignKey(User, default=None)
    #favorite_fruit= models.CharField(label='Choose Category', widget=models.Select(choices=cat_CHOICES))



    def __str__(self):
        return self.item_title

    # def snippet(self):
    #     return self.body[:50]+'...'



