from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_admin']


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('created_by', 'is_deleted')

        fields = ['candidate_fname', 'candidate_lname', 'candidate_email', 'candidate_phone', 'profile_heading',
                  'linkedin_url', 'skillset_1', 'skillset_2', 'skillset_3', 'skillset_4', 'skillset_5',
                  'experience_years', 'experience_months', 'current_location', 'prefered_location',
                  'notice_period']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['candidate_fname', 'candidate_lname', 'candidate_email', 'candidate_phone', 'profile_heading',
                  'linkedin_url', 'skillset_1', 'skillset_2', 'skillset_3', 'skillset_4', 'skillset_5',
                  'experience_years', 'experience_months', 'current_location', 'prefered_location',
                  'notice_period']
