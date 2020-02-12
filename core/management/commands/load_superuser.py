try:
    from django.core.management.base import NoArgsCommand as BaseCommand
except ImportError:
    from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load some sample data into the db"

    def handle(self, **options):
        from core.models import User
        from faker import Faker
        fake = Faker()

        print("Create superuser")
        data = {
            'username': 'admin',
            'email': 'admin@admin.com',
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        }
        superuser = User(**data)
        superuser.set_password('truong77')
        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save()