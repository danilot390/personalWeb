from django.contrib import admin
from django.urls import path, include

"""
URL configuration for trad project.
"""

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
