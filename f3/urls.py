from django.urls import path, include

from . import views
app_name = 'f3'
urlpatterns = [
    path('',views.c, name='f3')
]