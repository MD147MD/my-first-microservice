from django import forms




class QuestionCreationForm(forms.Form):
    title = forms.CharField(max_length=80,label='',
    widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control mb-3'}))
    body = forms.CharField(max_length=800,label='',
    widget=forms.Textarea(attrs={'placeholder':'Body','class':'form-control'}))