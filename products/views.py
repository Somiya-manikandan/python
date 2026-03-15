from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list.html',{'products':products})

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request,'products/product_form.html',{'form':form})

def update_product(request,id):
    product = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None,instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request,'products/product_form.html',{'form':form})

def delete_product(request,id):
    product = get_object_or_404(Product,id=id)

    if request.method=="POST":
        product.delete()
        return redirect('product_list')

    return render(request,'products/product_delete.html',{'product':product})