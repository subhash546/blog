from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Category,Blog,About 

from django.contrib.auth.decorators import login_required


def home(request):
   
    featured_posts=Blog.objects.filter(is_featured=True,status=1).order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status=1).order_by('updated_at')
    abouts=About.objects.all()
    context={
       
        'featuredposts':featured_posts,
        'posts':posts,
        'abouts':abouts
    }
    print(context)
    return render(request,"home.html",context)