from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.


def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully.')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'acconts/register.html', {'form': form})
