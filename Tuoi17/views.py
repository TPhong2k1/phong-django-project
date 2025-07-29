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
            return redirect('success')  # ✅ redirect đến trang thành công
    else:
        form = RegistrationForm()
    return render(request, 'Admin/register.html', {'form': form})

# Trang danh sách người đã đăng ký
def list_view(request):
    data = Registration.objects.all()
    return render(request, 'Admin/list.html', {'data': data})

# Trang thông báo gửi thành công
def success_view(request):
    return redirect('success')  # để tránh render lại POST