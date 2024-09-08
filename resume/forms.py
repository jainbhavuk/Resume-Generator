from django import forms
from .models import Profile

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            'name': 'Full Name',
            'education': 'Education',
            'skills': 'Skills',
            'workexperience': 'Work Experience',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'achievements':"Achievements"
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)