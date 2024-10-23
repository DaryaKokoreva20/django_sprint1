from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.about, name='about'),
    path('', views.rules, name='rules')
]
