from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup/register.html', {'form': form})


@login_required
def administrator(request):
    form_product = forms.FormName()
    if not request.user.is_superuser:
        return HttpResponse('The user is not an admin. Go Back.')
    else:
        if request.method == "POST":
            form_product = forms.FormName(request.POST)
            if form_product.is_valid():
                form_product.save()
        return render(request, 'signup/administrator.html', {'administrator': form_product})
