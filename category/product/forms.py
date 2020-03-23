from django import forms
from .import models

class AddProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['item_title','category', 'description', 'price', 'quantity','sku','thumb']