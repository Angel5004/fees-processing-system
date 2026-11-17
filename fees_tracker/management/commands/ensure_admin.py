import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create the default administrator if one does not exist'

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get('ADMIN_USERNAME')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write('Admin environment variables are missing.')
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write('Admin account already exists.')
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(self.style.SUCCESS('Admin account created!'))