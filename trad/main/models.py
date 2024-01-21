from django.db import models
from django.contrib.auth.models import User

class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return f'About Me @{self.user.username}'

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=250, default = '')

    def __str__(self):
        return f'Contact Me @{self.user.username}'
    
    def get_link_ti_whatsapp(self):
        return f"https://wa.me/{self.phone_number}?text=I'm%20interested%20in%20your%20proffesional%20services."

class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 240)
    url = models.CharField(max_length = 250)

    def __str__(self):
        return f'{self.social_media} @{self.user.username}'
    
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=150)
    slug = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.service} @{self.user.username}'
    
class New(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    ranking = models.IntegerField()
    hidden = models.BooleanField(default = False)


    def __str__(self) -> str:
        return f'New: {self.title}/{self.hidden}'