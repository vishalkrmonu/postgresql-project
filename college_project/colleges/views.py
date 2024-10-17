from django.shortcuts import render, redirect, get_object_or_404
from .models import College
from .forms import CollegeForm

def home(request):
    colleges = College.objects.all()
    return render(request, 'colleges/home.html', {'colleges': colleges})

def add_college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CollegeForm()
    return render(request, 'colleges/add.html', {'form': form})

def update_college(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        form = CollegeForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CollegeForm(instance=college)
    return render(request, 'colleges/update.html', {'form': form})

def delete_college(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        college.delete()
        return redirect('home')
    return render(request, 'colleges/delete.html', {'college': college})
