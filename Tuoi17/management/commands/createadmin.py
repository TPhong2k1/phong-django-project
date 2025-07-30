from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Tạo superuser admin nếu chưa có'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='banchihuy@gmail.com',
                password='banchihuy@'
            )
            self.stdout.write(self.style.SUCCESS("✅ Đã tạo superuser 'admin'"))
        else:
            self.stdout.write("⚠️ Superuser 'admin' đã tồn tại")