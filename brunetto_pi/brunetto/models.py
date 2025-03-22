from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Position(BaseModel):
    name = models.CharField(max_length=100)


class Employee(BaseModel):
    name = models.CharField(max_length=100)
    registration_number = models.IntegerField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')


class Pasta(BaseModel):
    name = models.CharField(max_length=100)

class ProductionDailyRecord(BaseModel):
    author = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='authored_records')
    production_leader = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='led_records')
    date = models.DateField()
    finished_pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name='massa_acabadas')
    quantity = models.IntegerField()
    waste = models.FloatField()
