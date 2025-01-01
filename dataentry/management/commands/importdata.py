from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Subscriber
from django.apps import apps
import csv
# Proposed command: python manage.py importdata file_path model_name

class Command(BaseCommand):
    help='Imports data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        # We write logic
        file_path=kwargs['file_path']
        model_name=kwargs['model_name'].capitalize()

        model=None
        # Search for the model accross all istalled apps
        for app_config in apps.get_app_configs():
            # Try to search for the model
            try:
                model=apps.get_model(app_config.label, model_name)
                break # Stop searching once the odel is found
            except LookupError:
                continue # Model not found in this app, continue searching in next app

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')


        with open(file_path, 'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                email=row['email']
                existing_record=model.objects.filter(email=email).exists()
                if not existing_record:
                    model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully!'))