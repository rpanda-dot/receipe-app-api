"""
Django Command to wait for the database to available
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError



class Command(BaseCommand):
    """ Django Command to wait for the database """

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("Waiting for database....")
        db_up = False
        while(db_up):
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database Available'))