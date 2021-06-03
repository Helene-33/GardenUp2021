from django.shortcuts import render
from .models import Plant, PlantType, Tips

# Create your views here.
def index(request):
    return render(request, 'gardenapp/index.html')

def plants(request):
    plant_list=Plant.objects.all()
    return render(request, 'gardenapp/plants.html', {'plant_list': plant_list})
    
