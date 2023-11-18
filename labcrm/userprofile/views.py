from django.contrib.auth.decorators import login_required
from .forms import ClientRegistrationForm, LabStaffRegistrationForm

from django.shortcuts import render, redirect
from .models import UserProfile


def signup(request, role='client'):
    if role == 'client':
        form_class = ClientRegistrationForm
    elif role == 'lab_staff':
        form_class = LabStaffRegistrationForm
    else:
        return redirect('home')  # or some default

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/log-in/')
    else:
        form = form_class()

    return render(request, 'userprofile/signup.html', {'form': form})


login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')