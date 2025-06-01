from django.shortcuts import render, redirect
from .forms import InternshipForm

# Create your views here.
from django.shortcuts import render
from .models import Internship

def internship_view(request):
    internship = Internship.objects.first()
    return render(request, 'experiences/internship.html', {'internship': internship})


def add_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('internship')  # Change to your success page or internship list page
    else:
        form = InternshipForm()
    return render(request, 'experiences/add_internship.html', {'form': form})
