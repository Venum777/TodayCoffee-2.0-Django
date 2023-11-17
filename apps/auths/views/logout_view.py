# Django
from django.views import View
from django.shortcuts import redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.contrib.auth import logout


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
