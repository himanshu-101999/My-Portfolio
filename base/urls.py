from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path("",views.home),   
    path("about/",views.about),
    path("contact/",views.contect),
    path("skills/",views.skills),
    path("project/",views.project),
    path("certificate/",views.certificate),
]
