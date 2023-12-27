from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    is_admin = models.BooleanField()
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['password1', 'password2']


class Profile(models.Model):
    # fields = ['candidate_fname', 'candidate_lname', 'candidate_email', 'candidate_phone','profile_heading','linkedin_url', 'skillset_1', 'skillset_2', 'skillset_3','skillset_4','skillset_5',
    candidate_fname = models.CharField(max_length=100, blank=False)
    candidate_lname = models.CharField(max_length=100, blank=False)
    candidate_email = models.EmailField()
    candidate_phone = models.CharField(max_length=15, blank=True)
    profile_heading = models.CharField(max_length=1000, blank=False)
    linkedin_url = models.CharField(max_length=1000, blank=True)
    Skill_TYPE_CHOICES = (
        ('Java', "Java"),
        ('SQL', "SQL"),
        ('Python Scripting', "Python Scripting"),
    )
    skillset_1 = models.CharField(
        max_length=100,
        choices=Skill_TYPE_CHOICES,
        blank=False
    )
    skillset_2 = models.CharField(
        max_length=100,
        choices=Skill_TYPE_CHOICES,
        blank=True
    )
    skillset_3 = models.CharField(
        max_length=100,
        choices=Skill_TYPE_CHOICES,
        blank=True
    )
    skillset_4 = models.CharField(
        max_length=100,
        choices=Skill_TYPE_CHOICES,
        blank=True
    )
    skillset_5 = models.CharField(
        max_length=100,
        choices=Skill_TYPE_CHOICES,
        blank=True
    )
    # 'experience_years','experience_months', 'current_location','prefered_location', 'notice_period']
    experience_years = models.IntegerField(blank=True)
    experience_months = models.IntegerField(blank=True)
    LOCATION_TYPE_CHOICES = (
        ('Mumbai', "Mumbai"),
        ('Gurgaon', "Gurgaon"),
        ('NCR', "NCR"),
    )
    current_location = models.CharField(
        max_length=100,
        choices=LOCATION_TYPE_CHOICES,
        blank=True
    )
    prefered_location = models.CharField(
        max_length=100,
        choices=LOCATION_TYPE_CHOICES,
        blank=True
    )
    notice_period = models.IntegerField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by', blank=True,
                                   null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "candidate_details"
