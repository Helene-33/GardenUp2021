from django.test import TestCase
from django.contrib.auth.models import User 
from .models import PlantType, Plant, Tips

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
