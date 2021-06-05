from django.shortcuts import render, get_object_or_404
from .models import Plant, PlantType, Tips
from django.urls import reverse_lazy
from .forms import PlantForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'gardenapp/index.html')

def plants(request):
    plant_list=Plant.objects.all()
    return render(request, 'gardenapp/plants.html', {'plant_list': plant_list})

def plantDetail(request, id):
    plant=get_object_or_404(Plant, pk=id)
    return render(request, 'gardenapp/plantdetail.html', {'plant' : plant})

@login_required
def newPlant(request):
    form=PlantForm
    if request.method== 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            post= form.save(commit=True)
            post.save()
            form=PlantForm()
    else:
        form=PlantForm()
    return render(request, 'gardenapp/newplant.html', {'form': form})

def loginmessage(request):
    return render(request, 'gardenapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'gardenapp/logoutmessage.html')