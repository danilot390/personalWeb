from django.db import models
from django.contrib.auth.models import User

class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='aboutmes')
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'About Me @{self.user.username}'

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='contacts')
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=250, default = '')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Contact Me @{self.user.username}'
    
    def get_link_to_whatsapp(self):
        return f"https://wa.me/{self.phone_number}?text=I'm%20interested%20in%20your%20professional%20services."

class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='socialmedias')
    social_media = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 240, blank = True )
    url = models.URLField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.social_media} @{self.user.username}'
    
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='services')
    service = models.CharField(max_length=150)
    slug = models.CharField(max_length=60)
    description = models.TextField()
    resumen = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.service} @{self.user.username}'
    
class New(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    ranking = models.IntegerField()
    hidden = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'New: {self.title}/{self.hidden}'
    
class Testimony(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='testimonys')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank = True, null=True)
    is_active = models.BooleanField(default = True)
    user_position = models.CharField( max_length=50)
    opinion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='messages', blank=True, null=True)
    type = models.CharField(max_length = 50, default='contact me')
    email = models.EmailField(max_length = 200)
    person = models.CharField(max_length=150)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)