from django.core.management.base import BaseCommand


# Proposed command=python manage.py greeting name
# Proposed output=Hi {name}, Good Morning
class Command(BaseCommand):
    help='Greets the user'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies username')

    def handle(self, *args, **kwargs):
        # We write logic
        name=kwargs['name']
        greeting=f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.HTTP_INFO(greeting))