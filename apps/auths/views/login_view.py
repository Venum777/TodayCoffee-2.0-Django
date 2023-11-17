# Django
from django.views import View
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.forms.models import ModelFormMetaclass
from django.contrib.auth import login, authenticate

# Local
from auths.forms.login_form import LoginForm
from auths.models import MyUser


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
