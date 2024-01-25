from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['person', 'email', 'subject', 'message']
        widgets = {
            'person' : forms.TextInput(attrs={
                'class' : 'col-md-6 form-control',
                'placeholder' : 'Your name',
                'required' : True,
                'label' : None
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'col-md-6 form-control',
                'placeholder' : 'Your email',
                'required' : True
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject ',
                'required' : True
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : 5,
                'placeholder' : 'Message ',
                'required' : True
            }),
        }

        labels = {
            'person' : '', 
            'email' : '', 
            'subject' : '', 
            'message' : ''
        }
        label_suffix = ''
        