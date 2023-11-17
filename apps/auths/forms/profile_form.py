# Django
from django import forms

# Local
from auths.models import MyUser


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
