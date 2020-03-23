from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from .models import Maincat
from product.models import Product
from django.contrib import messages

# Create your views here.
def maincatIndex(request):
    catList = Maincat.objects.all().order_by('id')
    return render(request,'maincat/maincatIndex.html', {'catList':catList})

@login_required(login_url="/accounts/login/")
def maincatAdd(request):
    if request.method == 'POST':
        form =forms.AddCategory(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            # instance.author = request.user
            instance.save()
            return redirect('maincat:list')
    else:
        form = forms.AddCategory()
    return render(request, 'maincat/maincatAdd.html',{'form':form})
    
@login_required(login_url="/accounts/login/")
def maincatEdit(request, id):
    catRow = get_object_or_404(Maincat, pk=id)
    if request.method == "POST":
        form = forms.AddCategory(request.POST,  instance=catRow)
        if form.is_valid():
            catRow = form.save(commit=False)
            catRow.save()
            return redirect('maincat:list')
    else:
        form = forms.AddCategory(instance=catRow)
    return render(request, 'maincat/maincatEdit.html', {'form': form, 'id':id})

@login_required(login_url="/accounts/login/")
def maincatDelete(request, id):
    catRow = Maincat.objects.get(id=id)
    #productList = Product.objects.get(category=catRow.id).count()
    productList = Product.objects.filter(category=catRow.id).count()

    if (productList< 1):
        catRow.delete()
    else:     
        messages.info(request, "Info: There are products in the category.")
        return redirect('maincat:list')

    return redirect('maincat:list')






