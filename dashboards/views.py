from django.shortcuts import render,redirect
from blog.models import Blog,Category

from .forms import CategoryForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def dashboard(request):
    categories_count= Category.objects.all().count()
    blogs_count =Blog.objects.all().count()
    context={
        "categories_count":categories_count,
        "blogs_count":blogs_count
    }
    return render (request,"dashboard/dashboard.html",context)


def category(request):
    return render (request,"dashboard/category.html")


def categoryadd(request):
    if request.method == "POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        
        
        form =CategoryForm()
    context={
        "form":form
    }
    return render(request,"dashboard/addcategory.html",context)


def categoryEdit(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form=CategoryForm( request.POST,instance=category)
        if form.is_valid():
            form.save()
        return redirect("category")
    else:
        
     form= CategoryForm(instance=category)
    context={
        "form":form,
        "category":category
    }
    
    return render(request,"dashboard/editcategory.html",context)

def categorydelete(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect("category")
