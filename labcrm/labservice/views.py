from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiagnosticServiceForm
from .models import DiagnosticService


@login_required
def labservice_list(request):
    service = DiagnosticService.objects.filter(created_by=request.user)

    return render(request, 'labservice/services_list.html', {
        'service': service
    })


login_required
def labservice_detail(request, pk):
    service = get_object_or_404(DiagnosticService, created_by=request.user, pk=pk)

    return render(request, 'labservice/service_detail.html', {
        'service': service
    })


login_required
def labservice_delete(request, pk):
    service = get_object_or_404(DiagnosticService, created_by=request.user, pk=pk)
    service.delete()
    messages.success(request, "The lab service was deleted")

    return redirect('labservice:list')


@login_required
def labservice_edit(request, pk):
    service = get_object_or_404(DiagnosticService, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = DiagnosticServiceForm(request.POST, instance=service)
        if form.is_valid():
            service.save()
            messages.success(request, "The lab service was created")

            return redirect('labservice:list')

    else:
        form = DiagnosticServiceForm(instance=service)

    return render(request, 'labservice/service_edit.html', {

        'form': form

    })


@login_required
def add_service(request):
    if request.method == 'POST':
        form = DiagnosticServiceForm(request.POST)

        if form.is_valid():
            service = form.save(commit=False)
            service.created_by = request.user
            service.save()
            messages.success(request, "The service was created")

            return redirect('labservice:list')
    else:
        form = DiagnosticServiceForm()

    return render(request, 'labservice/add_services.html', {

        'form': form

    })