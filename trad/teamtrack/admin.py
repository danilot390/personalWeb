from django.contrib import admin
from .models import Profile, Experience, ExperienceSkill, ExperienceDuty, Formation, FormationSkill, Achievement, Reference

class ExperienceSkillInline(admin.StackedInline):
    # Inline admin for ExperienceSkill model
    model = ExperienceSkill
    extra = 1

class ExperienceDutyInline(admin.StackedInline):
    # Inline admin for ExperienceDuty model
    model = ExperienceDuty
    extra = 1 

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    # Admin configuration for Experience model
    list_display = ('profile', 'position', 'company',)
    search_fields = ('profile__user__username', 'position', 'company',)
    inlines = [ExperienceSkillInline, ExperienceDutyInline]

class FormationSkillInline(admin.TabularInline):
    # Inline admin for FormationSkill model
    model = FormationSkill
    extra = 1

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    # Admin configuration for Formation model
    list_display = ('profile', 'institution', 'career',)
    search_fields = ('profile__user__username', 'institution', 'career',)
    inlines = [FormationSkillInline]
   
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    # Admin configuration for Achievement model
    list_display = ('profile', 'institution',)
    search_fields = ('profile__user__username', 'institution',)
   
@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    # Admin configuration for Reference model
    list_display = ('profile', 'reference',)
    search_fields = ('profile__user__username', 'reference',)

class ExperienceInline(admin.TabularInline):
    # Inline admin for Experience model
    model = Experience
    extra = 1
    inlines = [ExperienceSkillInline, ExperienceDutyInline] 

class FormationInline(admin.TabularInline):
    # Inline admin for Formation model
    model = Formation
    extra = 1
    inlines = [FormationSkillInline]

class AchievementInline(admin.TabularInline):
    # Inline admin for Achievement model
    model = Achievement
    extra = 1

class ReferenceInline(admin.TabularInline):
    # Inline admin for Reference model
    model = Reference
    extra = 1 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Admin configuration for Profile model
    list_display = ('user', 'profession',)
    search_fields = ('user__username', 'profession',)
    inlines = [ExperienceInline, FormationInline, AchievementInline, ReferenceInline]
