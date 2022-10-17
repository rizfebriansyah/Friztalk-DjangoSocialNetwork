from django import forms
from .models import UserPost, Remark

class UserPostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = UserPost
        fields = ('content', 'image')

class RemarkModelForm(forms.ModelForm):
    body = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'placeholder': 'Add a remark...'}))
    class Meta:
        model = Remark
        fields = ('body',)