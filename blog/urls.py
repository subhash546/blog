from django.urls import path,include
from .views import postby_category,singleBlog


urlpatterns = [
    path('<int:category_id>/',postby_category,name="post_by_category"),
    path('<slug:slug>/',singleBlog,name="single_blog"),
]
