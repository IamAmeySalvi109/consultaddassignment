from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

# Create your views here.


@login_required
def profiles(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
    else:
        u_form = UserUpdateForm(instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    context = {
        'u_form': u_form
    }
    return render(request, 'profiles/profiles.html', context)
