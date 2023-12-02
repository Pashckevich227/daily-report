from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Ваш Email',
        'type': 'email',
        'id': 'inputEmail'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Имя',
        'type': 'text'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Фамилия',
        'type': 'text'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Пароль',
        'type': 'password',
        'id': 'inputPassword'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Повторите пароль',
        'type': 'password',
        'id': 'inputPassword'
    }))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Ваш Email',
        'type': 'email',
        'id': 'inputEmail'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Пароль',
        'type': 'password',
        'id': 'inputPassword'
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
