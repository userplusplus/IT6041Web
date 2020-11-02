from django.shortcuts import render


def index(request):
    return render(request, 'IT6041App/index.html', {'title': 'GreenWorlds EcoStore'})

def staff(request):
    return render(request, 'IT6041App/staff.html', {'title': 'GreenWorlds EcoStore'})

