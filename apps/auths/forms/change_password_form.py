# Django
from django import forms

# Local
from auths.models import MyUser


class ChangePasswordForm(forms.ModelForm):
    """Registration form for CustomUser."""

    password = forms.CharField(
        label='Новый пароль',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Введите пароль'
            }
        )
    )

    password1 = forms.CharField(
        label='Новый пароль',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Введите новый пароль'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Повторите пароль',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Повторите пароль'
            }
        )
    )

    class Meta:
        model = MyUser
        fields = (
            'password',
        )

    def check_password(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit: bool = ...) -> MyUser:
        self.full_clean()
        return super().save(commit)
