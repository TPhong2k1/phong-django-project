from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

# Trang chủ quản trị
def admin_home(request):
    return render(request, 'Admin/admin_home.html')

# Trang đăng ký
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # 🔁 Chuyển sang trang danh sách sau khi gửi
    else:
        form = RegistrationForm()
    return render(request, 'Admin/register.html', {'form': form})

# Trang danh sách
def list_view(request):
    data = Registration.objects.all()
    return render(request, 'Admin/list.html', {'data': data})