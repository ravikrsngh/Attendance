from django import forms
from django.contrib.auth.models import User
from .models import *
class userform(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password')

class studentform(forms.ModelForm):
    class Meta():
        model = student
        fields = ('phone','sem','usn','branch','pic1','pic2','pic3','pic4','pic5','pic6','pic7','pic8','pic9','pic10','pic11','pic12','pic13','pic14','pic15')

class teacherform(forms.ModelForm):
    class Meta():
        model = teacher
        fields = ('phone','designation','department')

class imgform(forms.Form):
    img=forms.ImageField()
