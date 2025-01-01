from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help='Prints Hello World'

    def handle(self, *args, **kwargs):
        # We write logic
        self.stdout.write('Hlello World')