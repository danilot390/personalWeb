from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User

from about.models import image_path
from main.models import TimestampedModel

# Common abstract model for retrieving keywords associated with models
class KeywordMixin:
    # Method to retrieve keywords associated with the model
    def keywords(self):
        # Retrieve related skills
        related_skills = self.skills.all() 
        # Join related skills into a comma-separated string
        return ', '.join(str(skill.skill.skill) for skill in related_skills)
    
# Profile Model: Represents user profiles
class Profile(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='profiles')  # Link to user
    profession = models.CharField(_('Profession of the user'),max_length=150)  
    profile = models.TextField(_('Profile description')) 
    highlight = models.CharField(_('Highlighted information'),max_length=250 ) 
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return self.profession 
     


# Experience Model: Represents work experience of a user
class Experience(TimestampedModel, KeywordMixin):
    profile = models.ForeignKey(Profile, verbose_name=_("User Profile"), on_delete=models.CASCADE, related_name='experiences')  # Link to user profile
    position = models.CharField(_('Position held'),max_length=50) 
    company = models.CharField(_('Company name'), max_length=50) 
    start = models.DateField(_('Start date of experience')) 
    end = models.DateField(_('End date of experience'), null=True, blank=True) 
    active = models.BooleanField(_('Is currently active?'), default=False) 
    location = models.CharField(_('Location of experience'), max_length=100) 
    description = models.TextField(_('Description of experience')) 

    def __str__(self):
        return f"{self.position} at {self.company}"  

# ExperienceSkill Model: Represents skills related to work experience
class ExperienceSkill(TimestampedModel):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='skills')  # Link to experience
    skill = models.ForeignKey('about.Skill', on_delete=models.CASCADE, verbose_name=_("Skill"))  # Related skill

    def __str__(self):
        return f'{self.skill}'  

# ExperienceDuty Model: Represents duties/responsibilities in work experience
class ExperienceDuty(TimestampedModel):
    experience = models.ForeignKey(Experience, related_name='duties', on_delete=models.CASCADE)  # Link to experience
    duty = models.TextField(_('Duty/responsibility description'))

    def __str__(self):
        return f'{self.duty}'  

class Formation(TimestampedModel, KeywordMixin):
    # Choices for the type of degree field
    DEGREE_CHOICES = [
        ("Bachelor", _("Bachelor's Degree")),
        ("Master", _("Master's Degree")),
        ("Doctorate", _("Doctorate")),
        ("Diploma", _("Diploma")),
        ("Certificate", _("Certificate")),
        ("Associate", _("Associate Degree")),
        ("Vocational Training", _("Vocational Training")),
        ("Professional Qualifications", _("Professional Qualifications")),
    ]

    profile = models.ForeignKey(Profile, verbose_name=_("User Profile"), related_name='formations', on_delete=models.CASCADE)  # Link to user profile
    institution = models.CharField(_("Institution name"), max_length=100) 
    location = models.CharField(_("Location of Institution"), max_length=100)  
    career = models.CharField(_("Career pursued"), max_length=100)   
    type_degree = models.CharField(_("Type of Degree"), max_length=30, choices=DEGREE_CHOICES)  # Adjusted max_length
    description = models.TextField(_("Description of formation"))  
    active = models.BooleanField(_('Is currently active?'), default=False) 
    start = models.DateField(_("Start date of formation"), auto_now=False, auto_now_add=False) 
    end = models.DateField(_("End date of formation"), auto_now=False, auto_now_add=False, null=True, blank=True)  

    def __str__(self):
        return f"{self.career} at {self.institution}"  
    

# FormationSkill Model: Represents skills related to educational formation
class FormationSkill(TimestampedModel):
    formation = models.ForeignKey(Formation, verbose_name=_("User Formation"), related_name='skills', on_delete=models.CASCADE)  # Link to formation
    skill = models.ForeignKey('about.Skill', verbose_name=_("Skill"), on_delete=models.CASCADE)  # Related skill

    def __str__(self):
        return f'{self.skill}'  

# PortfolioSkill Model: Represents skills related to project in portfolio
class PortfolioSkill(TimestampedModel):
    project = models.ForeignKey('about.Portfolio', on_delete=models.CASCADE, related_name='skills')  # Link to experience
    skill = models.ForeignKey('about.Skill', on_delete=models.CASCADE, verbose_name=_("Skill"))  # Related skill

    def __str__(self):
        return f'{self.skill}'  
# Achievement Model: Represents achievements
class Achievement(TimestampedModel):
    profile = models.ForeignKey(Profile, verbose_name=_("User Profile"), related_name='achievements', on_delete=models.CASCADE)  # Link to user profile
    institution = models.CharField(_("Institution name"), max_length=100)  
    description = models.TextField(_("Description of Achievement"))  
    date = models.DateField(_("Date of Achievement"), auto_now=False, auto_now_add=False, null = True, blank=True)  

    def __str__(self):
        return f'{self.description} at {self.institution}'  

# Reference Model: Represents references
class Reference(TimestampedModel):
    profile = models.ForeignKey(Profile, verbose_name=_("User Profile"), related_name='references', on_delete=models.CASCADE)  # Link to user profile
    reference = models.TextField(_("Reference"))  # Reference text

    def __str__(self):
        return self.reference  