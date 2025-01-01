from django.core.management.base import BaseCommand
from dataentry.models import Subscriber

# I want to add some data to the database using the custom command

class Command(BaseCommand):
    help='It will insert data to the database'

    def handle(self, *args, **kwargs):
        # We write logic
        dataset=[
            {'name':'SATYAM', 'email':'sv8865997@gmail.com'},
            {'name':'KUNTALA', 'email':'sv8865997@gmail.com'},
        ]
        for data in dataset:
            name=data['name']
            email=data['email']
            existing_record=Subscriber.objects.filter(email=email).exists()
            if not existing_record:
                Subscriber.objects.create(name=name, email=email)
                self.stdout.write(self.style.SUCCESS(f'Subscriber with email ID: {email} entered into our record'))
            else:
                self.stdout.write(self.style.WARNING(f'Subscriber with email ID: {email} already exists in our record'))        
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))