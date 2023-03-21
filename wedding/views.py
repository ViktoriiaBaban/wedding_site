from django.shortcuts import render
import datetime
from .models import Guest
from django.views.generic import ListView, CreateView

def guests_attend(request):
    if request.method == 'POST':
        fio = request.POST['fio']
        attend = request.POST['attend']

        Guest.objects.create(fio=fio, attend=attend)
        return render(request, 'index.html', {'success': True})
    else:
        return render(request, 'index.html')

class AllGuests(ListView):
    model = Guest
    template_name = 'list.html'

