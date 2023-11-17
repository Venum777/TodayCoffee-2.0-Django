# Django
from django import forms

# Local
from auths.models import MyUser


class RegisterForm(forms.ModelForm):
    """Registration form for CustomUser."""
    
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
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password'
        )
        widgets = {
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Пароль'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Почта'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Имя'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Фамилия'
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Номер телефона'
                }
            )
        }

    def save(self, commit: bool = ...) -> MyUser:
        self.full_clean()
        return super().save(commit)
