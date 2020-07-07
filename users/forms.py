from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = ('email',)
