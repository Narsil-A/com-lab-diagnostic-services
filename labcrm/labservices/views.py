from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DiagnosticServiceForm


@login_required
def add_service(request):
    if request.method == 'POST':
        form = DiagnosticServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.created_by = request.user
            service.save()
            messages.success(request, "The service was created")

            return redirect('service_list')
    else:
        form = DiagnosticServiceForm()

    return render(request, 'labservices/add_services.html', {

        'form': form

    })