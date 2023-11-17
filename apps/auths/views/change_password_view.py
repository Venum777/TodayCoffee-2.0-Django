# Django
from django.views import View
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.forms.models import ModelFormMetaclass
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Local
from auths.forms.change_password_form import ChangePasswordForm
from auths.models import MyUser


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
