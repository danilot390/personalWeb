from django.contrib import admin
from .models import Contact, New, Message, SocialMedia, Testimony, SocialUser, SocialCompany

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    """
    list_display = ('user', 'phone_number', 'location', 'created_at', 'updated_at')
    search_fields = ('user__username', 'phone_number', 'location')

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the New model.
    """
    list_display = ('title', 'ranking', 'hidden', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SocialMedia model.
    """
    list_display = ('name', 'slug', 'url', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'url')

@admin.register(SocialUser)
class SocialUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SocialUser model.
    """
    list_display = ('user', 'name', 'slug', 'url', 'created_at', 'updated_at')
    search_fields = ('user__username', 'name', 'slug', 'url')

@admin.register(SocialCompany)
class SocialCompanyAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SocialCompany model.
    """
    list_display = ('company', 'name', 'slug', 'url', 'created_at', 'updated_at')
    search_fields = ('company__name', 'name', 'slug', 'url')

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Testimony model.
    """
    list_display = ('user', 'service', 'is_active', 'user_position', 'opinion', 'created_at', 'updated_at')
    search_fields = ('user__username', 'service__service', 'user_position', 'opinion')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Message model.
    """
    list_display = ('user', 'type', 'email', 'person', 'subject', 'is_read', 'created_at', 'updated_at')
    search_fields = ('user__username', 'type', 'email', 'person', 'subject', 'message')
