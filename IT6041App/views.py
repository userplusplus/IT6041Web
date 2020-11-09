from django.shortcuts import render

from . models import Staff
from django.views.generic import (ListView)

def index(request):
    return render(request, 'IT6041App/index.html', {'title': 'GreenWorlds EcoStore'})

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'IT6041App/staff.html', {'title': 'GreenWorlds EcoStore', 'staff' : staff})


class TaskListView(ListView):
    model = Staff
    template_name = 'IT6041App/staff.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'staff'
    ordering = ['-staff_full_name']

