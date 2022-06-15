from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import request,response
from django.contrib.auth import get_user_model

class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = forms.FileField()
    class Meta:
        model=get_user_model()
        fields =("email","username",'password1','password2','profile_image')

    def save(self, commit=True):
     
        image = self.cleaned_data['profile_image']
        fss = FileSystemStorage('image/')
        file = fss.save(image.name, image)
        user = super(UserRegistration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.profile_image = self.cleaned_data.get('profile_image')
        if commit:
            user.save()
        return user

