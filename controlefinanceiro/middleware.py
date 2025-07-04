from django.shortcuts import render
from django.urls import resolve
from django.conf import settings

EXEMPT_VIEW_NAMES = [
    'login',
    'register',
    'admin:login',
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            resolver_match = resolve(request.path_info)
            if resolver_match.view_name not in EXEMPT_VIEW_NAMES:
                return render(request, 'erro_login.html', status=403)
        return self.get_response(request)
