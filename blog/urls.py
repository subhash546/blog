from django.urls import path,include
from .views import postby_category,singleBlog,search,register


urlpatterns = [
     path('search/',search,name="search"),
    path('<int:category_id>/',postby_category,name="post_by_category"),
    path('blogs/<slug:slug>/',singleBlog,name="single_blog"),
   
   
]
