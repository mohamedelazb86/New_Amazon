from django.urls import path
from .views import Product_list,Product_Detail

urlpatterns = [
    path('',Product_list.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
]
