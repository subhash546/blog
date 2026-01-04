from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Category,Blog

def home(request):
   
    featured_posts=Blog.objects.filter(is_featured=True,status=1).order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status=1).order_by('updated_at')
    context={
       
        'featuredposts':featured_posts,
        'posts':posts
    }
    print(context)
    return render(request,"home.html",context)