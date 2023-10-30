'''AUTHS VIEWS'''
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.forms.models import ModelFormMetaclass
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import InMemoryUploadedFile

#Local
from .forms import (
    RegisterForm, 
    LoginForm, 
    ChangePasswordForm, 
    ProfileForm
)
from .models import MyUser
from abstracts.utils import generate_string


class RegisterView(View):
    """Registration View."""

    template_name = 'register.html'
    form: ModelFormMetaclass = RegisterForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'reg_form': self.form()
            }
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        form: RegisterForm = self.form(
            request.POST
        )
        if not form.is_valid():
            return HttpResponse("BAD")

        custom_user: MyUser = form.save(
            commit=False
        )
        custom_user.password =\
            make_password(custom_user.password)

        custom_user.save()
        return redirect('login')
    
class LoginView(View):
    """Login View."""

    template_name: str = 'login.html'
    form: ModelFormMetaclass = LoginForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'log_form' : self.form()
            }
        )

    def post(
         self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        form: LoginForm = self.form(
            request.POST
        )
        if not form.is_valid():
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    'log_form' : self.form()
                }
            )
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user: MyUser = authenticate(
            username=email,
            password=password
        )
        if not user:
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    'log_form' : self.form()
                }
            )
        login(request, user)

        return redirect('home')


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


class LogoutView(View):
    """Logout View."""

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        if request.user:
            logout(request)
        
        return redirect('home')


class ChangePasswordView(View):
    """Change password View."""


    template_name: str = 'change_password.html'
    form: ModelFormMetaclass = ChangePasswordForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'ch_pass_form' : self.form()
            }
        )
    
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        user_id = request.user.id
        form: ChangePasswordForm = self.form(
            request.POST
        )
        if not form.is_valid():
            return HttpResponse("BAD")
        if not check_password(form.cleaned_data['password'], request.user.password):
            return HttpResponse("Неправильный пароль")
        form.check_password()
        custom_user: MyUser = form.save(
            commit=False
        )
        password = custom_user.password = make_password(form.cleaned_data['password1'])
        MyUser.objects.update_user(
            user_id=user_id,
            password=password
        )
        return redirect('login')
