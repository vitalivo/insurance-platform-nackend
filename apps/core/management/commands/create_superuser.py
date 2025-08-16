from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Создает суперпользователя если он не существует'

    def handle(self, *args, **options):
        # Получаем данные из переменных окружения
        username = config('DJANGO_SUPERUSER_USERNAME', default='admin')
        email = config('DJANGO_SUPERUSER_EMAIL', default='goshkoxxx@inbox.ru')
        password = config('DJANGO_SUPERUSER_PASSWORD', default='admin123')

        # Проверяем, существует ли уже суперпользователь
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.WARNING('Суперпользователь уже существует')
            )
            return

        # Создаем суперпользователя
        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Суперпользователь "{username}" успешно создан')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Ошибка создания суперпользователя: {e}')
            )