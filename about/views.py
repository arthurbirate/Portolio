from django.shortcuts import render, redirect
from .forms import AboutMeForm
from .models import AboutMe

def about_me_view(request):
    about = AboutMe.objects.first()
    return render(request, 'about/about.html', {'about': about})

def add_about(request):
    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_me')  
    else:
        form = AboutMeForm()
    return render(request, 'about/add_about.html', {'form': form})