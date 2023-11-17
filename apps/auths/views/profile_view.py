# Django
from django.views import View
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from auths.forms.profile_form import ProfileForm
from auths.models import MyUser
from abstracts.utils import generate_string


class ProfileView(View):
    """Profile View."""

    template_name: str = 'profile.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    )-> HttpResponse:
        form: ProfileForm = ProfileForm(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone_number': request.user.phone_number
            }
        )
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user': request.user,
                'ctx_form': form
            }
        )
    
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    )-> HttpResponse:
        form: ProfileForm = ProfileForm(
            request.POST,
            request.FILES
        )
        first_name: str = request.POST.get('first_name')
        last_name: str = request.POST.get('last_name')
        email: str = request.POST.get('email')
        phone_number: str = request.POST.get('phone_number')
        user_id: MyUser = request.user.id
        profile_picture: InMemoryUploadedFile =\
        request.FILES.get('profile_picture')

        profile_picture.name = generate_string() + ".png"

        form.update_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            # profile_picture=profile_picture
        )

        return redirect('profile')