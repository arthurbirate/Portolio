from django.shortcuts import get_object_or_404, render, redirect
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
            return redirect('internship')  
    else:
        form = InternshipForm()
    return render(request, 'experiences/add_internship.html', {'form': form})



def edit_internship(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    if request.method == 'POST':
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            return redirect('internship')  
    else:
        form = InternshipForm(instance=internship)
    return render(request, 'experiences/edit_internship.html', {'form': form, 'internship': internship})