
from django import forms
from .models import MyUser


# class RegisterForm(forms.ModelForm):
#     """Registration form for CustomUser."""
    
#     password2 = forms.CharField(
#         label='Повторите пароль',
#         max_length=100,
#         widget=forms.PasswordInput()
#     )
#     class Meta:
#         model = MyUser
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#             'phone_number',
#             'password'
#         )
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

#     def save(self, commit: bool = ...) -> MyUser:
#         self.full_clean()
#         return super().save(commit)


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