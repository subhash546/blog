from django.urls import path

from .views import dashboard,category,categoryadd

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('/category',category,name="category"),
    path('/category/add',categoryadd,name="Addcategory")
]