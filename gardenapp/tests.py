from gardenapp.views import newPlant
from gardenapp.forms import PlantForm
from django.test import TestCase
from django.contrib.auth.models import User 
from .models import PlantType, Plant, Tips
import datetime
from .forms import PlantForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class PlantTypeTest(TestCase):
    def setUp(self):
        self.type=PlantType(typename='Outdoor shady')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Outdoor shady')

    def test_tablename(self):
        self.assertEqual(str(PlantType._meta.db_table), 'planttype')

class PlantTest(TestCase):
    def setUp(self):
        self.type=PlantType(typename='Outdoor shady')
        self.user= User(username='user1')
        self.plant = Plant(plantname= 'Digitalis (Foxglove)', planttype=self.type, user=self.user, dateentered='03/06/2021', price= 49.99, planturl= 'https://www.gardeningknowhow.com/ornamental/flowers/foxglove/' , description="Digitalis" )

    def test_string(self):
        self.assertEqual(str(Plant), 'Digitalis (Foxglove)')

    def test_discount(self):
        disc= self.plant.price * .20
        self.assertEqual(self.plant.discountAmount(),disc)

    def test_discountAmount(self):
        self.assertEqual(self.plant.discountPrice(), 39.92)

class NewPlantForm(TestCase):
    def test_plantform(self):
        data={
            'plantname':'Daisy', 
            'planttype': 'Outdoor shady', 
            'user':'helene', 
            'dateentered':'03/06/2021', 
            'price':'5.99',
            'planturl': 'https://www.thespruce.com/daisy-types-for-gardens-1316051',
            'description': 'Gorgeous daisies blumming for months!'
            }
        form=PlantForm (data)
        self.assertTrue(form.is_valid)

    def test_plantform_Invalide(self):
        data={
            'plantname':'Daisy', 
            'planttype': 'Outdoor shady', 
            'user':'helene', 
            'dateentered':'03/06/2021', 
            'planturl': 'https://www.thespruce.com/daisy-types-for-gardens-1316051',
            'description': 'Gorgeous daisies blumming for months!'
            }
        form=PlantForm (data)
        self.assertFalse(form.is_valid)

class New_Plant_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create(username='testuser1', password='Cesaire23')
        self.type=Type.objects.create(typename='Indoor sunny')
        self.plant=Plant.objects.create(plantname= 'Digitalis (Foxglove)', planttype=self.type, user=self.user, dateentered='03/06/2021', price= 49.99, planturl= 'https://www.gardeningknowhow.com/ornamental/flowers/foxglove/' , description="Digitalis" )

    def test_redirect_if_not_logged_in(self):
        response.self.client.get(reverse('newPlant'))
        self.assertRedirects(response, 'accounts/login/?next=/gardenapp/newplant/')
