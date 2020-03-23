from django import forms
from .import models

class AddCategory(forms.ModelForm):
    class Meta:
        model = models.Maincat
        fields = ['category']