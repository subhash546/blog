from django.shortcuts import render,redirect
from blog.models import Blog,Category

from .forms import CategoryForm,PostForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


def posts(request):
    posts=Blog.objects.all()
    context={
        "posts":posts
    }
    return render (request,"dashboard/posts.html",context)


def addposts(request):
    if request.method == "POST":
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            title=form.cleaned_data['title']
            post.slug= slugify(title) 
            post.save()
            post.slug= f"{post.slug}-{post.id}"
            post.save(update_fields=['slug'])
            return redirect("posts")     
    else:
            
      form=PostForm()
    context={
        "form":form
    }
    
    return render (request,"dashboard/addposts.html",context)


def editpost(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            title=form.cleaned_data['title']
            post.slug= slugify(title) 
            post.save()
            post.slug= f"{post.slug}-{post.id}"
            post.save(update_fields=['slug'])
            return redirect("posts") 
            
    form =PostForm(instance=post) 
    context={
      'form':form,
      'post':post
    }
    return render(request,"dashboard/editpost.html",context)


def deletepost(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect("posts")


def users(request):
    user= User.objects.all()
    context={
        "user":user
    }
    
    return render(request,"dashboard/users.html",context)