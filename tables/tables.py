import django_tables2 as tables
from .models import Pcb

class PcbTable(tables.Table):
    class Meta:
        model = Pcb
