from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **options):
        
        from django.core.management import call_command
        
        call_command('loaddata', 'collections.json')
        call_command('loaddata', 'products.json')
