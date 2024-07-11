from django.utils import timezone
from django.contrib import messages

class CheckAutomationStatusMixin:
    def check_automation_status(self, request):
        automations = self.get_queryset(request)
        now = timezone.now()
        for automation in automations:
            print(f" \nAgora{now} ")
            print(f"\nultimo {automation.last_ping }")
            if automation.last_ping and (now - automation.last_ping).total_seconds() > 300:  # 5 minutos em segundos
                automation.is_active = False
                automation.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
