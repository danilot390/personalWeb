from django.urls import path
from about.views import load_about

app_name = 'about'

urlpatterns = [
    # Define a URL pattern for the 'load_about'view
    path('about/', load_about, name='load_about'),
]
