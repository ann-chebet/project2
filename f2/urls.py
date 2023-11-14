from django.urls import path, include

from . import views
app_name = 'f2'
urlpatterns = [
    path('',views.b, name='f2')
]