from django import forms
from .models import Profile

class ProfilePageModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('f_name', 'l_name', 'biography', 'profile_picture')