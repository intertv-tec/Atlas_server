from django.contrib import admin
from django.utils import timezone
from .models import Automation
from .admin_mixins import CheckAutomationStatusMixin

class AutomationAdmin(CheckAutomationStatusMixin, admin.ModelAdmin):
    list_display = ['name', 'is_active', 'last_ping']
    list_filter = ['is_active']
    search_fields = ['name']

    def changelist_view(self, request, extra_context=None):
        self.check_automation_status(request)
        self.message_user(request, "Status das automações verificado com sucesso.")
        return super().changelist_view(request, extra_context)

admin.site.register(Automation, AutomationAdmin)
