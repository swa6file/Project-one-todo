from django import forms

class SupportUserForm(forms.Form):
    title = forms.CharField(label="Название",widget=forms.TextInput(attrs={'class':'form-input'}))
    description = forms.CharField(label="Описание",widget=forms.Textarea(attrs={'class':'form-control','id':'taskDescription','rows':'3','placeholder':"Введите описание проблемы"}))