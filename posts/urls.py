from django.urls import path
from .views import post_detail,post_list,create_post,delete_post,update_post

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    
    path('update_post/<slug:slug>',update_post),
    path('delete_post/<slug:slug>',delete_post)
]

