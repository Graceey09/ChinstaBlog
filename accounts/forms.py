from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Profile

User = get_user_model()


class RegisterForm(forms.ModelForm):
    phone = forms.CharField(max_length=11, label='Phone Number')
    image = forms.ImageField(label='Image')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone', 'image')
