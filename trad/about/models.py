from django.db import models
from django.contrib.auth.models import User
import os

# Company Model: Model for Company information
class Company(models.Model):
    name = models.CharField(max_length=150)
    slang = models.CharField(max_length=50)
    slogan = models.TextField()
    description = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    background = models.TextField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=250, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} at: {self.updated_at}'
    
    def get_link_to_whatsapp(self, message):
        # Generate a link to whatsapp using the phone number with a specific message
        return f"https://wa.me/{self.phone_number}?text={message}"

# ServiceCompany Model: Model for Services offered by a Company
class ServiceCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')
    service = models.CharField(max_length=150)
    slug = models.CharField(max_length=60)
    description = models.TextField()
    resumen = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.service} @{self.company.name}'

def image_path(instance, filename, path='user'):
    # Get the file extension
    ext = filename.split('.')[-1]
    
    # Determine the model name
    model_name = instance.__class__.__name__.lower()
    
    # Rename the file for the current model
    filename = f'{model_name}_{instance.id}_image.{ext}'

    # Return the new path
    return os.path.join(model_name, filename)

# Employee Model: Model for Employee information
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employee')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    position = models.CharField(max_length=50)
    duties = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='none.jpg', upload_to=image_path)
    
    def __str__(self):
        return f'{self.user.username} - {self.position}'
     
# Values Model: Model for Company values
class Values(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    value = models.CharField(max_length=150)
    slang = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.slang} : {self.value}'

# TypeProject Model: Model types of projects
class TypeProject(models.Model):
    name = models.CharField(max_length=50)
    slang = models.CharField(max_length=15)
    description = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Portfolio Model: Model for portfolio of employees
class Portfolio(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name='portfolio')
    type_project = models.ForeignKey("TypeProject", on_delete=models.CASCADE, related_name='portfolio', null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    keywords = models.CharField(max_length=150)
    urls = models.URLField(max_length=200, null=True, blank=True)
    git = models.URLField(max_length=200, null=True, blank=True)
    weight = models.IntegerField()
    image = models.ImageField(default='none.jpg', upload_to=image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} @{self.employee.user}'

# Skill Model: Model for Skills
class Skill(models.Model):
    skill = models.CharField(max_length=150)
    slang = models.CharField(max_length=20)
    keywords = models.CharField(max_length=250)
    image = models.ImageField(default='none.jpg', upload_to=image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.skill} : {self.keywords}'

# EmployeeModel: Model for Skills of employees
class EmployeeSkill(models.Model):
    empployee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name = 'skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.empployee} - {self.skill}'