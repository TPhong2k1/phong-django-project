from django.apps import AppConfig

class Tuoi17Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tuoi17'

    def ready(self):
        # Gọi auto tạo superuser ở đây
        from phong.auto_superuser import create_super_user
        create_super_user()