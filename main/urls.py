from django.urls import path
from main.views import index, about, welcome

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome")
]