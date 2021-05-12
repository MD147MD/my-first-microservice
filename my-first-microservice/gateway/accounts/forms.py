from django import forms



class RegisterForm(forms.Form):
    email = forms.CharField(max_length=120,label=''
    ,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}))
    full_name = forms.CharField(max_length=80,label=''
    ,widget=forms.TextInput(attrs={'placeholder':'Full Name','class':'form-control'}))
    password = forms.CharField(max_length=100,label=''
    ,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    password_confirm = forms.CharField(max_length=100,label=''
    ,widget=forms.PasswordInput(attrs={'placeholder':'Password Confirm','class':'form-control'}))

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Password And Password Confirm Does Not Match')
        return cd['password']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=120,label=''
    ,widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}))
    password = forms.CharField(max_length=100,label=''
    ,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))