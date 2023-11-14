from django.urls import path, include

from . import views
app_name = 'f4'
urlpatterns = [
    path('', views.d, name='f4')
    ]