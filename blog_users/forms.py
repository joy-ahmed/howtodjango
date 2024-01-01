from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'user_role', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )

    avatar = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )

    user_role = forms.ChoiceField(
        choices=USER_ROLE,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return email
    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2



class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('first_name','last_name','email','avatar', 'bio', 'user_role')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'user_role': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
        }
        


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )



class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )




class CustomPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password'}),
    )
    new_password2 = forms.CharField(
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your new password'}),
    )