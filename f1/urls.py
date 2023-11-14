from django.urls import path, include




from . import views
app_name = 'fi'
urlpatterns = [
    path('',views.a, name='fi')
]