from django import forms
from .models import Student

# class Stu(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     city=forms.CharField()
#     age=forms.IntegerField()


class Studentform(forms.ModelForm):
        class Meta:
            model=Student
            fields='__all__'


