from django.shortcuts import render
from django.utils.timezone import now

def home(request):
    # Pass current year for footer
    context = {
        'now': now(),
    }
    return render(request, 'home.html', context)