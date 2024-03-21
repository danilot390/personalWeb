from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User

from main.models import Testimony
from about.models import Company, ServiceCompany

from main.forms import MessageForm

def load_index (request):
    """
    Render the index page with information about the company and a message form.
    
    Retrieves details about the company, including contact information, social media links, and 
    vailable services. Active testimonials are fetched for display. The MessageForm is instantiated
    in the context to allow users to submit inquieres or feedback.

    Args:
        request: The request object.
    Returns:
        HttpResponse: Rendered template with context data.
    """

    
    # Objects
    testimonials = Testimony.objects.filter(is_active=True)

    # Instantiate the MessageForm
    message_form = MessageForm()

    # Prepare the context dictionary
    context = {
        'testimonials' : testimonials,
        'messageForm' : message_form,
    }

    # Render the template with the context
    return render(request, 'main/index.html', context)

def process_message_form(request):
    """
    Handles form submission and saves messages to the database.

    Args:
        request (HttpRequest): The request object
    Return:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            success_message = 'Your message has been sent. Thank You!'
            return redirect(reverse('main:index'))
        
        # If the form is not valid or the request method is not POST,
        # redirect back to the index form page
        return redirect(reverse('main:index'))