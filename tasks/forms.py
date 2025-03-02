from django import forms

class AddPostTask(forms.Form):
    title = forms.CharField(max_length=100,label='Название задачи',widget=forms.TextInput(attrs={'type':'text','class':'form_control','id':"taskTitle", 'placeholder':"Введите заголовок задачи"}))
    description = forms.CharField(max_length=500,label='Описание',widget=forms.Textarea(attrs={'class':'form-control','id':'taskDescription','rows':'3','placeholder':"Введите описание задачи"}))

