from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Company model.
    """
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ServiceCompany model.
    """
    list_display = ('company', 'service', 'created_at', 'updated_at')
    search_fields = ('company__name', 'service')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Employee model.
    """
    list_display = ('user', 'company', 'position', 'created_at', 'updated_at')
    search_fields = ('user__username', 'company__name', 'position')

@admin.register(Values)
class ValuesAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Values model.
    """
    list_display = ('company', 'value', 'slang', 'created_at', 'updated_at')
    search_fields = ('company__name', 'value', 'slang')

@admin.register(TypeProject)
class TypeProjectAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TypeProject model.
    """
    list_display = ('name', 'slang', 'created_at', 'updated_at')
    search_fields = ('name', 'slang')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Portfolio model.
    """
    list_display = ('employee', 'type_project', 'name', 'created_at', 'updated_at')
    search_fields = ('employee__user__username', 'type__name', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Skill model.
    """
    list_display = ('skill', 'slang', 'created_at', 'updated_at')
    search_fields = ('skill', 'slang')

@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for the EmployeeSkill model.
    """
    list_display = ('empployee', 'skill', 'created_at', 'updated_at')
    search_fields = ('empployee__user__username', 'skill__skill')