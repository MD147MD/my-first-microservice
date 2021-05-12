from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name','email')
    
    def save(self,commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password(self):
        cd = self.changed_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Password And Password Confirm Does Not Match')
        return cd['password']


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','email')
    

    def clean_password(self):
        self.initial['password']