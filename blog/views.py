from django.shortcuts import get_object_or_404, render,redirect

from .models import Blog,Category

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

