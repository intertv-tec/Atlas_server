from celery import shared_task
from django.utils import timezone
from .models import Automation

@shared_task
def check_automation_status():
    automations = Automation.objects.all()
    now = timezone.now()
    for automation in automations:
        if automation.last_ping and (now - automation.last_ping).total_seconds() > 300:  # 5 minutos em segundos
            automation.is_active = False
            automation.save()
