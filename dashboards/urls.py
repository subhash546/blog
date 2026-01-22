from django.urls import path

from .views import dashboard,category,categoryadd,categoryEdit,categorydelete,posts,addposts,deletepost,editpost,users,adduser,edituser

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('/category',category,name="category"),
    path('/category/add',categoryadd,name="Addcategory"),
    path('/category/edit/<int:pk>/',categoryEdit,name="Editcategory"),
    path('/category/delete/<int:pk>/',categorydelete,name="deletecategory"),
    
    #posts
    path('/posts',posts,name="posts"),
    path('/posts/add',addposts,name="AddPosts"),
    path('post/edit/<int:pk>',editpost,name="EditPost"),
    path('post/delete/<int:pk>/',deletepost,name="deletepost"),
    
    #users
    path('/users',users,name="users"),
    path('/add/users',adduser,name="adduser"),
    path('/edit/users/<int:pk>/',edituser,name="edituser")
    
]