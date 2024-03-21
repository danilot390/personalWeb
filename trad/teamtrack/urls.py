from django.urls import path
from teamtrack.views import profile_team

app_name = 'teamtrack'

urlpatterns = [
    # Define a URL pattern for accessing a user's profile by their ID
    # The profile_team view will be responsible for rendering the profile page
    path('profile/<int:id>/', profile_team, name='profile'),
]