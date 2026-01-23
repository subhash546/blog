from django.shortcuts import get_object_or_404, render,redirect

from .models import Blog,Category,Comment
from .form import RegisterForm

from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth 
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def postby_category(request,category_id):
    posts=Blog.objects.filter(status=1,category=category_id)
    try:
        category=Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return redirect("home")
    #category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'ca':category
    }
    return render(request,"postbycategory.html",context)


def singleBlog(request,slug):
    singleBlog=get_object_or_404(Blog,slug=slug,status=1)
    if request.method == "POST":
        comment=Comment()
        comment.user=request.user
        comment.blog=singleBlog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path)
    comment= Comment.objects.filter(blog=singleBlog)
    counter=Comment.objects.filter(blog=singleBlog).count()
    context={
        'singleBlog':singleBlog,
        'comment':comment,
        "counter":counter
    }
    return render(request,"singleblog.html",context)



def search(request):
    query=request.GET.get('text')
    posts=Blog.objects.filter(Q(title__icontains=query)| Q(short_description__icontains=query)| Q(blog_body__icontains=query),status=1)
    context={
        'posts':posts,
        'query':query
    }
    return render(request,"search.html",context)



def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
    
      form=RegisterForm()
    context={
        "form":form
    }
    
    return render(request,"register.html",context)
    
    
    
def login(request):
    if request.method == "POST":
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
           user=form.get_user()
           auth.login(request,user)
           return redirect("dashboard")  
        else :
            messages.error(request, 'Invalid username or password')
              
    form=AuthenticationForm()
    context={
        "form":form
    }
    return render(request,"login.html",context)


def logout(request):
    auth.logout(request)
    return redirect("login")
