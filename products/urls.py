from django.urls import path
from .views import Product_list,Product_Detail,add_review,Brand_detail,Brand_list

urlpatterns = [
    path('brands',Brand_list.as_view()),
    path('brands/<slug:slug>',Brand_detail.as_view()),
    
    path('',Product_list.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
    path('<slug:slug>/add_review',add_review),
]
