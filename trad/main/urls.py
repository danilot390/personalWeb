from django.urls import path
from main.views import load_index, process_message_form

app_name = 'main'

urlpatterns = [
    path('',load_index, name='index'),
    path('process_message/',process_message_form, name='proccess_message'),
]
