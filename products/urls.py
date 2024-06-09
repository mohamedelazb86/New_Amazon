from django.urls import path
from .views import Product_list,Product_Detail,add_review

urlpatterns = [
    path('',Product_list.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
    path('<slug:slug>/add_review',add_review),
]
