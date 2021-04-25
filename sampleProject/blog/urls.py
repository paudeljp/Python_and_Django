from django.urls import path

from blog.views import *

urlpatterns = [
    path('list/', blog_list),
    path('detail/<int:id>/', blog_detail),
]