# authapp/management/commands/progress_report_reminders.py
from django.core.management.base import BaseCommand
from authapp.views import send_progress_report_reminders
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Send progress report reminders'

    def handle(self, *args, **options):
        try:
            send_progress_report_reminders()
            self.stdout.write(self.style.SUCCESS('Progress report reminders sent successfully'))
        except Exception as e:
            logger.error(f'Error sending progress report reminders: {e}')
            self.stdout.write(self.style.ERROR('Error sending progress report reminders'))
