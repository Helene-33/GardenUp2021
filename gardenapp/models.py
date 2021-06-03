from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

class PlantType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='planttype'
        verbose_name_plural='planttypes'

class Plant(models.Model):
    plantname=models.CharField(max_length=255)
    planttype=models.ForeignKey(PlantType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    planturl=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.plantname

    class Meta:
        db_table='plant'
        verbose_name_plural='plants'

class Tips(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plant=models.ForeignKey(Plant, on_delete=models.CASCADE)
    tipdate=models.DateField()
    tiptext=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table='tips'