from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True


class Position(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(BaseModel):
    
    name = models.CharField(max_length=100)
    registration_number = models.PositiveIntegerField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f'{self.name} - {self.position.name}'

class Pasta(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Stuffing(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class ProductionDailyRecord(BaseModel):
    author = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='authored_records')
    production_leader = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='led_records')
    date = models.DateField()

    def __str__(self):
        return f"Registro de {self.date.strftime('%d/%m/%Y')} - Líder: {self.production_leader.name}"

class FinishedPasta(BaseModel):
    production_record = models.ForeignKey(ProductionDailyRecord, on_delete=models.CASCADE, related_name='finished_pastas')
    finished_pasta = models.ForeignKey(Pasta, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    waste = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f"{self.finished_pasta} - {self.quantity} unidades"


class InProgressPasta(BaseModel):
    production_record = models.ForeignKey(ProductionDailyRecord, on_delete=models.CASCADE, related_name='in_progress_pastas')
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='in_progress_pasta_employees')
    in_progress_pasta = models.ForeignKey(Pasta, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.in_progress_pasta

class PastaMachine(BaseModel):
    production_record = models.ForeignKey(ProductionDailyRecord, on_delete=models.CASCADE, related_name='pasta_machine_usages')
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='machine_usage_employees')
    machine = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.machine} masseiras usadas"

class PastaCooking(BaseModel):
    production_record = models.ForeignKey(ProductionDailyRecord, on_delete=models.CASCADE, related_name='cooked_pastas')
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='pasta_cooking_employees')
    pasta_cooking = models.ForeignKey(Pasta, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    discard = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f'Colaborador: {self.employee} - Cozimento: {self.pasta_cooking}'

class PastaStuffing(BaseModel):
    production_record = models.ForeignKey(ProductionDailyRecord, on_delete=models.CASCADE, related_name='pasta_stuffings')
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='pasta_stuffing_employees')
    stuffing = models.ForeignKey(Stuffing, null=True, blank=True, on_delete=models.SET_NULL)
    recipes = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Colaborador: {self.employee} - Recheio: {self.stuffing}'
