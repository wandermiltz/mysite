from django.shortcuts import render
from django.utils import timezone
from .models import Pcb
from .models import Status
#from .tables import PcbTable

def index(request):
   #pcbs = Pcb.objects.all
   pcbs = Pcb.objects.filter(status='В работе')
   return render(request, 'tables/index.html', {'pcbs': pcbs})

#def index(request):
#    table = PcbTable(Pcb.objects.all())
#    return render(request, 'tables/index.html', {'table': table})
