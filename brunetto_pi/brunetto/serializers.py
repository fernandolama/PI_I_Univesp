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

class FinishedPastaNestedSerializerRecord(serializers.ModelSerializer):
    finished_pasta_id = serializers.IntegerField(write_only=True)
    finished_pasta = SimplePastaSerializer(read_only=True)

    class Meta:
        model = FinishedPasta
        fields = ['id', 'finished_pasta_id', 'finished_pasta', 'quantity', 'waste']

class InProgressPastaNestedSerializerRecord(serializers.ModelSerializer):
    in_progress_pasta_id = serializers.IntegerField(write_only=True)
    in_progress_pasta = SimplePastaSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    employee = SimpleEmployeeSerializer(read_only=True)

    class Meta:
        model = InProgressPasta
        fields = ['id', 'employee_id', 'employee', 'in_progress_pasta_id', 'in_progress_pasta', 'quantity']

class PastaMachineNestedSerializerRecord(serializers.ModelSerializer):
    employee_id = serializers.IntegerField(write_only=True)
    employee = SimpleEmployeeSerializer(read_only=True)

    class Meta:
        model = PastaMachine
        fields = ['id', 'employee_id', 'employee', 'machine']

class PastaCookingNestedSerializerRecord(serializers.ModelSerializer):
    pasta_cooking_id = serializers.IntegerField(write_only=True)
    pasta_cooking = SimplePastaSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    employee = SimpleEmployeeSerializer(read_only=True)

    class Meta:
        model = PastaCooking
        fields = ['id', 'employee_id', 'employee', 'pasta_cooking_id', 'pasta_cooking', 'quantity', 'discard']

class PastaStuffingNestedSerializerRecord(serializers.ModelSerializer):
    stuffing_id = serializers.IntegerField(write_only=True)
    stuffing = StuffingSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    employee = SimpleEmployeeSerializer(read_only=True)

    class Meta:
        model = PastaStuffing
        fields = ['id', 'employee_id', 'employee', 'stuffing_id', 'stuffing', 'recipes']

class ProductionDailyRecordCompleteSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    author = SimpleEmployeeSerializer(read_only=True)
    production_leader_id = serializers.IntegerField(write_only=True)
    production_leader = SimpleEmployeeSerializer(read_only=True)

    finished_pastas = FinishedPastaNestedSerializerRecord(many=True, write_only=True, required=False)
    in_progress_pastas = InProgressPastaNestedSerializerRecord(many=True, write_only=True, required=False)
    pasta_machine_usages = PastaMachineNestedSerializerRecord(many=True, write_only=True, required=False)
    cooked_pastas = PastaCookingNestedSerializerRecord(many=True, write_only=True, required=False)
    pasta_stuffings = PastaStuffingNestedSerializerRecord(many=True, write_only=True, required=False)

    finished_pastas_read = FinishedPastaNestedSerializerRecord(source='finished_pastas', many=True, read_only=True)
    in_progress_pastas_read = InProgressPastaNestedSerializerRecord(source='in_progress_pastas', many=True, read_only=True)
    pasta_machine_usages_read = PastaMachineNestedSerializerRecord(source='pasta_machine_usages', many=True, read_only=True)
    cooked_pastas_read = PastaCookingNestedSerializerRecord(source='cooked_pastas', many=True, read_only=True)
    pasta_stuffings_read = PastaStuffingNestedSerializerRecord(source='pasta_stuffings', many=True, read_only=True)

    class Meta:
        model = ProductionDailyRecord
        fields = [
            'id',
            'author_id', 'author',
            'production_leader_id', 'production_leader',
            'date',

            'finished_pastas',
            'in_progress_pastas',
            'pasta_machine_usages',
            'cooked_pastas',
            'pasta_stuffings',

            'finished_pastas_read',
            'in_progress_pastas_read',
            'pasta_machine_usages_read',
            'cooked_pastas_read',
            'pasta_stuffings_read',
        ]

    def create(self, validated_data):
        finished_pastas = validated_data.pop('finished_pastas', [])
        in_progress_pastas = validated_data.pop('in_progress_pastas', [])
        pasta_machine_usages = validated_data.pop('pasta_machine_usages', [])
        cooked_pastas = validated_data.pop('cooked_pastas', [])
        pasta_stuffings = validated_data.pop('pasta_stuffings', [])

        record = ProductionDailyRecord.objects.create(
            author_id=validated_data.pop('author_id'),
            production_leader_id=validated_data.pop('production_leader_id'),
            **validated_data
        )

        self._create_nested(FinishedPasta, finished_pastas, record, {
            'finished_pasta_id': Pasta,
        }, fk_field='production_record')

        self._create_nested(InProgressPasta, in_progress_pastas, record, {
            'in_progress_pasta_id': Pasta,
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaMachine, pasta_machine_usages, record, {
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaCooking, cooked_pastas, record, {
            'pasta_cooking_id': Pasta,
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaStuffing, pasta_stuffings, record, {
            'stuffing_id': Stuffing,
            'employee_id': Employee,
        }, fk_field='production_record')

        return record


    def update(self, instance, validated_data):
        finished_pastas = validated_data.pop('finished_pastas', [])
        in_progress_pastas = validated_data.pop('in_progress_pastas', [])
        pasta_machine_usages = validated_data.pop('pasta_machine_usages', [])
        cooked_pastas = validated_data.pop('cooked_pastas', [])
        pasta_stuffings = validated_data.pop('pasta_stuffings', [])

        instance.date = validated_data.get('date', instance.date)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.production_leader_id = validated_data.get('production_leader_id', instance.production_leader_id)
        instance.save()

        instance.finished_pastas.all().delete()
        instance.in_progress_pastas.all().delete()
        instance.pasta_machine_usages.all().delete()
        instance.cooked_pastas.all().delete()
        instance.pasta_stuffings.all().delete()

        self._create_nested(FinishedPasta, finished_pastas, instance, {
            'finished_pasta_id': Pasta,
        }, fk_field='production_record')

        self._create_nested(InProgressPasta, in_progress_pastas, instance, {
            'in_progress_pasta_id': Pasta,
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaMachine, pasta_machine_usages, instance, {
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaCooking, cooked_pastas, instance, {
            'pasta_cooking_id': Pasta,
            'employee_id': Employee,
        }, fk_field='production_record')

        self._create_nested(PastaStuffing, pasta_stuffings, instance, {
            'stuffing_id': Stuffing,
            'employee_id': Employee,
        }, fk_field='production_record')

        return instance


    def _create_nested(self, model_class, data_list, parent_instance, id_field_mapping, fk_field):
        for item in data_list:
            for id_field, model in id_field_mapping.items():
                if id_field in item:
                    real_field = id_field.replace('_id', '')
                    item[real_field] = model.objects.get(id=item.pop(id_field))
            item[fk_field] = parent_instance
            model_class.objects.create(**item)