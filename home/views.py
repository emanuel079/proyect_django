from django.contrib.auth import (
    authenticate,
    login, 
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View


# Create your views here.
class LoginView(View):

    def get(self, request):
        return render(
            request,
            'home/login.html'
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


@login_required(login_url='login')
def index_view(request):
    return render(
        request,
        'home/index.html'
    )



