from django.urls import path,include
from .views import postby_category


urlpatterns = [
    path('<int:category_id>/',postby_category,name="post_by_category")
]
