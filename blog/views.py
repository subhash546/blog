from django.shortcuts import get_object_or_404, render,redirect

from .models import Blog,Category
from .form import RegisterForm

from django.db.models import Q

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
    context={
        'singleBlog':singleBlog
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
    

