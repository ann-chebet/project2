from django.urls import path, include

from . import views
app_name = 'f1'
urlpatterns = [
    path('',views.a, name='f1')
]