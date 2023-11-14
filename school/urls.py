
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("f1.urls")),
    path('f2/', include("f2.urls")),
    path('f3/', include("f3.urls")),
    path('f4/', include("f4.urls"))
# branch2