
from django import forms
from .models import MyUser


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

class ProfileForm(forms.ModelForm):
    """Registration form for CustomUser."""

    profile_picture = forms.FileField(
        label='Изменить фото профиля'
    )
    class Meta:
        model = MyUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile_picture',
        )

    def update_user(self, user_id, **kwargs):
        user = MyUser.objects.get(id=user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
            
        user.save()
        return user