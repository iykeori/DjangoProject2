from django.shortcuts import render, redirect, render_to_response
from maincat.models import Maincat
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.template import RequestContext
from django.shortcuts import get_object_or_404, redirect, render, reverse


# Create your views here.
def productIndex(request):
    #catList = Maincat.objects.all().order_by('title')
    productList = Product.objects.all()
    return render(request,'product/productIndex.html', {'productList':productList})

@login_required(login_url="/accounts/login/")
def productAdd(request):
    if request.method == 'POST':
        form =forms.AddProduct(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            # instance.author = request.user
            instance.save()
            return redirect('product:list')
    else:
        form = forms.AddProduct()
    return render(request, 'product/productAdd.html',{'form':form})


@login_required(login_url="/accounts/login/")
def productEdit(request, id):
    productRow = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = forms.AddProduct(request.POST, request.FILES, instance=productRow)
        if form.is_valid():
            productRow = form.save(commit=False)
            productRow.save()
            return redirect('product:list')
    else:
        form = forms.AddProduct(instance=productRow)
    return render(request, 'product/productEdit.html', {'form': form, 'id':id})


@login_required(login_url="/accounts/login/")
def productDelete(request, id):
    productRow = Product.objects.get(id=id)
    productRow.delete()
    return redirect('product:list')



