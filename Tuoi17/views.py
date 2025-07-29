from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

# Trang chủ quản trị
def admin_home(request):
    return render(request, 'Tuoi17/admin_home.html')

# Trang đăng ký
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tuoi17/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'tuoi17/register.html', {'form': form})

# Trang danh sách
def list_view(request):
    data = Registration.objects.all()
    return render(request, 'tuoi17/list.html', {'data': data})