from django.contrib import admin
from .models import Pcb, Status


class PcbAdmin(admin.ModelAdmin):
    fields = ['code','pcb_name', 'quantity','customer', 'pcb_code', 'revision_code', 'status']
    list_display = ('code','pcb_name', 'quantity','customer', 'pcb_code', 'revision_code', 'status')
    search_fields = ['pcb_name']
    list_filter = ['status', 'customer']

admin.site.register(Pcb, PcbAdmin)

class StatusAdmin(admin.ModelAdmin):
    fields = ['code','status']
    list_display = ('code','status')

admin.site.register(Status, StatusAdmin)
