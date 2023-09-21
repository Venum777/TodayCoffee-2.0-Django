'''AUTHS VIEWS'''

from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


class LoginView(View):
    """
    User login.
    """

    def get(self, request: WSGIRequest) -> HttpResponse:
        ...

    def post(self, request: WSGIRequest) -> HttpResponse:
        ...


class RegisterView(View):
    """
    User login.
    """

    template_name = 'register.html'

    def get(self, request: WSGIRequest) -> HttpResponse:
        pass

    def post(self, request: WSGIRequest) -> HttpResponse:
        pass