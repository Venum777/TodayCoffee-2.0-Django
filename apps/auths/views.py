'''AUTHS VIEWS'''
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate
from django.forms.models import ModelFormMetaclass
from django.contrib.auth.hashers import make_password

#Local
from .forms import RegisterForm, LoginForm
from .models import MyUser


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

    template_name: str = 'profile.html'

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    )-> HttpResponse:
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user': request.user
            }
        )
    
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    )-> HttpResponse:
        if request.method == 'POST':
            user_id = request.user.id
            first_name: str = request.POST.get('first_name')
            last_name: str = request.POST.get('last_name')
            email: str = request.POST.get('email')
            phone_number: str = request.POST.get('phone_number')

            MyUser.objects.update_user(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
            )
            return redirect('home')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user': request.user
            }
        )
