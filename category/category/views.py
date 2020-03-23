from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product

def catIndex(request):
    #catList = Maincat.objects.all().order_by('title')
    productList = Product.objects.all()
    return render(request,'catIndex.html', {'productList':productList})


def catAdd(request):
    return render(request, 'catAdd.html')


def catEdit(request):
    return render(request, 'catEdit.html')