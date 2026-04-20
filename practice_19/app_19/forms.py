from django import forms
from .models import Emp
class StudentForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['name', 'age', 'email', 'phone', 'resume']
        # fields = '__all__'


class StudentLoginForm(forms.Form):
     
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput  # 🔑 Ye password ko hide karega
    )