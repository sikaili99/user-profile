from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('home_address', 'phone_number',
                  'picture', 'city', 'location',)
