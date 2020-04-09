from django import forms
from crud.models import Information


class InformationModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'id' : 'first_name',
            'placeholder': 'Enter First Name',
        }
    ))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'last_name',
            'placeholder': 'Enter Last Name',
        }
    ))
    father_name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'id':'father_name',
            'placeholder':'Enter Father Name',
        }
    ))
    mother_name = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'mother_name',
            'placeholder':'Enter Mother Name'
        }
    ))
    age = forms.CharField(max_length=3,widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'id': 'age',
            'placeholder':'Enter Your Age',
        }
    ))
    gender = forms.CharField(max_length=6, widget=forms.Select(choices=[('','Select'),('ml','Male'),('fm','Female')],
        attrs = {
            'class': 'form-control',
            'id':'gender',
        }
    ))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(
        attrs = {
            'class':'form-control',
            'id':'email',
            'placeholder':'Enter Your Email',
        }
    ))
    password_first = forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'id': 'password_first',
            'name':'password_first',
            'placeholder':'Enter Password',
        }
    ))
    password_last = forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'id': 'password_last',
            'name':'password_last',
            'placeholder':'Enter Password Again',
        }
    ))
    
    class Meta:
        model = Information
        fields = ['first_name','last_name','father_name','mother_name','age','gender','email','password_first','password_last']
