from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect('relatorio-financeiro')  # Redireciona após cadastro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
