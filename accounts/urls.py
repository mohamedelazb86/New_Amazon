from django.urls import path
from .views import signup,activate,dashbord

urlpatterns = [
    path('signup',signup),
    path('<str:username>/activate',activate),
    path('dasbord',dashbord),
]
