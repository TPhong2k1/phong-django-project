from django.contrib.auth import get_user_model

# ✅ Tạo superuser nếu chưa có
def create_super_user():
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'banchihuy@gmail.com', 'banchihuy@')
        print("✅ Superuser 'admin' đã được tạo!")

