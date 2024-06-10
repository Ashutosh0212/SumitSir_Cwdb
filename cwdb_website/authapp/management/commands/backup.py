# authapp/management/commands/progress_report_reminders.py
from django.core.management.base import BaseCommand
from authapp.views import dump_whole_backup
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'take and Send backup'

    def handle(self, *args, **options):
        try:
            dump_whole_backup()
            self.stdout.write(self.style.SUCCESS('backup sent successfully'))
        except Exception as e:
            logger.error(f'Error sending backup: {e}')
            self.stdout.write(self.style.ERROR('Error sending backup'))
