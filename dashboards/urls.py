from django.urls import path

from .views import dashboard,category,categoryadd,categoryEdit,categorydelete

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('/category',category,name="category"),
    path('/category/add',categoryadd,name="Addcategory"),
    path('/category/edit/<int:pk>/',categoryEdit,name="Editcategory"),
    path('/category/delete/<int:pk>/',categorydelete,name="deletecategory"),
    
]