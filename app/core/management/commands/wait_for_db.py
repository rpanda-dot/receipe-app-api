"""
Django Command to wait for the database to available
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django Command to wait for the database """

    def handle(self, *args, **options):
        pass