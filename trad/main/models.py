from django.db import models
from django.contrib.auth.models import User
from about.models import ServiceCompany, Company

# Common abstract model for timestamped fields
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Contact Model: Represents contact information for a user
class Contact(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='contacts')
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'Contact Me @{self.user.username}'
    
    # Generates a link to WhatsApp using the phone number with a specific message
    def get_link_to_whatsapp(self, message):
        return f"https://wa.me/{self.phone_number}?text={message}"

# SocialMedia Model: Represents social media information
class SocialMedia(TimestampedModel):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=240, blank=True)
    url = models.URLField(max_length=250)

    def __str__(self):
        return f'{self.name}'

# SocialUser Model: Inherits from SocialMedia, adds a ForeignKey relationship with User model
class SocialUser(SocialMedia):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='socialmedias')  

# SocialCompany Model: Inherits from SocialMedia, adds a ForeignKey relationship with Company model
class SocialCompany(SocialMedia):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='socialmedias')

# New Model: Represents news 
class New(TimestampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    ranking = models.IntegerField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'New: {self.title}/{self.hidden}'
    
# Testimony Model: Represents user testimonials
class Testimony(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='testimonys')
    service = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user_position = models.CharField(max_length=50)
    opinion = models.TextField()

    def __str__(self):
        return f'{self.user.username} : {self.opinion}'

# Message Model: Represents user or not user messages
class Message(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='messages', blank=True, null=True)
    type = models.CharField(max_length=50, default='contact me')
    email = models.EmailField(max_length=200)
    person = models.CharField(max_length=150)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}{self.person}: {self.message}'
