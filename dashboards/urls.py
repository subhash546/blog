from django.urls import path

from .views import dashboard,category

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('/category',category,name="category"),
]