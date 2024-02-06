from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def schedule_progress_report_reminders():
    try:
        from django.core.management import call_command
        call_command('progress_report_reminders')
        logger.info('Scheduled task to send progress report reminders executed successfully')
    except Exception as e:
        logger.error(f'Error executing scheduled task to send progress report reminders: {e}')


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authapp"
    
    def ready(self):
        scheduler = BackgroundScheduler()
        if settings.DEBUG:
            scheduler.add_job(schedule_progress_report_reminders, trigger='interval', minutes=1, id='progress_report_reminders_job')  # Run every minute in debug mode
        else:
            scheduler.add_job(schedule_progress_report_reminders, trigger='cron', hour='*/6', id='progress_report_reminders_job')  # Run every 6 hours in production mode
        scheduler.start()