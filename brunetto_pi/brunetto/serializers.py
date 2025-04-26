# serializers.py
from rest_framework import serializers
from .models import Position, Employee, Pasta, Stuffing, ProductionDailyRecord, FinishedPasta, InProgressPasta, PastaMachine, PastaCooking, PastaStuffing

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        
class EmployeePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')
        
class RegistrationNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'registration_number')

class GetEmployeeSerializer(serializers.ModelSerializer):    
    position = EmployeePositionSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Employee
        fields = '__all__'

class PastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasta
        fields = '__all__'

class StuffingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuffing
        fields = '__all__'

class ProductionDailyRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionDailyRecord
        fields = '__all__'

class ProductionDailyRecordsCompleteSerializer(serializers.ModelSerializer):
    author = EmployeePositionSerializer(read_only=True)
    production_leader = EmployeePositionSerializer(read_only=True)    
    class Meta:
        model = ProductionDailyRecord
        fields = '__all__'
   

        
class FinishedPastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedPasta
        fields = '__all__'

class InProgressPastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InProgressPasta
        fields = '__all__'

class PastaMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastaMachine
        fields = '__all__'

class PastaCookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastaCooking
        fields = '__all__'

class PastaStuffingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastaStuffing
        fields = '__all__'
        
class ProductionDailyRecordSerializer(serializers.ModelSerializer):
    finished_pasta = FinishedPastaSerializer(read_only=True)
    in_progress_pasta = InProgressPastaSerializer(read_only=True)
    pasta_machine = PastaMachineSerializer(read_only=True)
    pasta_cooking = PastaCookingSerializer(read_only=True)
    pasta_stuffing = PastaStuffingSerializer(read_only=True)
    class Meta:
        model = ProductionDailyRecord
        fields = '__all__'
        
class SimpleEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')

class SimplePastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasta
        fields = ('id', 'name')

class SimpleStuffingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuffing
        fields = ('id', 'name')
        
class FinishedPastaNestedSerializer(serializers.ModelSerializer):
    finished_pasta = SimplePastaSerializer(read_only=True)

    class Meta:
        model = FinishedPasta
        fields = ('id', 'finished_pasta', 'quantity', 'waste')

class InProgressPastaNestedSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)
    in_progress_pasta = SimplePastaSerializer(read_only=True)

    class Meta:
        model = InProgressPasta
        fields = ('id', 'employee', 'in_progress_pasta', 'quantity')

class PastaMachineNestedSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)

    class Meta:
        model = PastaMachine
        fields = ('id', 'employee', 'machine')

class PastaCookingNestedSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)
    pasta_cooking = SimplePastaSerializer(read_only=True)

    class Meta:
        model = PastaCooking
        fields = ('id', 'employee', 'pasta_cooking', 'quantity', 'discard')

class PastaStuffingNestedSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)
    stuffing = SimpleStuffingSerializer(read_only=True)

    class Meta:
        model = PastaStuffing
        fields = ('id', 'employee', 'stuffing', 'recipes')

class ProductionDailyRecordCompleteSerializer(serializers.ModelSerializer):
    author             = SimpleEmployeeSerializer(read_only=True)
    production_leader  = SimpleEmployeeSerializer(read_only=True)

    # transformamos o nested em SerializerMethodField
    finished_pastas      = serializers.SerializerMethodField()
    in_progress_pastas   = serializers.SerializerMethodField()
    pasta_machine_usages = serializers.SerializerMethodField()
    cooked_pastas        = serializers.SerializerMethodField()
    pasta_stuffings      = serializers.SerializerMethodField()

    class Meta:
        model = ProductionDailyRecord
        fields = [
            'id',
            'author',
            'production_leader',
            'date',
            'finished_pastas',
            'in_progress_pastas',
            'pasta_machine_usages',
            'cooked_pastas',
            'pasta_stuffings',
        ]

    def get_finished_pastas(self, obj):
        qs = obj.finished_pastas.filter(finished_pasta__isnull=False)
        return FinishedPastaNestedSerializer(qs, many=True).data

    def get_in_progress_pastas(self, obj):
        qs = obj.in_progress_pastas.filter(in_progress_pasta__isnull=False)
        return InProgressPastaNestedSerializer(qs, many=True).data

    def get_pasta_machine_usages(self, obj):
        qs = obj.pasta_machine_usages  # ou aplique filtro se precisar
        return PastaMachineNestedSerializer(qs, many=True).data

    def get_cooked_pastas(self, obj):
        qs = obj.cooked_pastas.filter(pasta_cooking__isnull=False)
        return PastaCookingNestedSerializer(qs, many=True).data

    def get_pasta_stuffings(self, obj):
        qs = obj.pasta_stuffings.filter(stuffing__isnull=False)
        return PastaStuffingNestedSerializer(qs, many=True).data