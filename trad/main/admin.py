from django.contrib import admin
from .models import AboutMe, Contact, New, Message, SocialMedia, Service, Testimony

@admin.register(AboutMe)
class AboutmeAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedia)
class SocialmediaAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass