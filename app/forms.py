from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from string import ascii_letters


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email already exists')


class ProfileForm(forms.ModelForm):

    phone = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    account_number = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    bank = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ("phone", "account_number", "bank")
