from django.shortcuts import render,redirect
from .forms import UserRegister
from django.contrib import messages
# Create your views here.

def Register(request):

    if request.method == "POST":
        form = UserRegister(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()

            user = form.cleaned_data.get('user')
            messages.success=(f'Your account {user} is now active please login and view our content')
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form':form})
