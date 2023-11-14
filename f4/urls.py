from django.urls import path, include

from . import views
app_name = 'fa'
urlpatterns = [
    path('', views.d, name='fa')
    ]
