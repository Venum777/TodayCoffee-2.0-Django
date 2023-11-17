# Django
from django import forms

# Local
from auths.models import MyUser


class LoginForm(forms.Form):
    """Login form for CustomUser."""
    
    email = forms.EmailField(
        label='Почта',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Почта'
                }
            )
    )
    password = forms.CharField(
        label='Пароль',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Пароль'
                }
            )
    )
    class Meta:
        model = MyUser
        fields = (
            'email',
            'password'
        )
