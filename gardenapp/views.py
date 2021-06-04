from django.shortcuts import render, get_object_or_404
from .models import Plant, PlantType, Tips

# Create your views here.
def index(request):
    return render(request, 'gardenapp/index.html')

def plants(request):
    plant_list=Plant.objects.all()
    return render(request, 'gardenapp/plants.html', {'plant_list': plant_list})

def plantDetail(request, id):
    plant=get_object_or_404(Plant, pk=id)
    return render(request, 'gardenapp/plantdetail.html', {'plant' : plant})
