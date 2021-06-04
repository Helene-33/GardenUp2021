from django import forms
from .models import PlantType, Plant, Tips

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields='__all__'