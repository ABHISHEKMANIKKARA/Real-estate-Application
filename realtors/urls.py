from django.urls import path
from . import views

urlpatterns = [
    path('realtors/', views.realtors,name="realtors"),
    #path('about/',views.about,name="about"),
]