from django import forms
class Studentform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField()
    city=forms.CharField()

# from .models import Student
# class Studentform(forms.ModelForm):
#     class Meta:
#         model=Student
        

