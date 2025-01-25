from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('gallery', views.gallery, name='gallery'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]