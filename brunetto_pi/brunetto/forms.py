from django import forms
from django.forms import inlineformset_factory
from .models import *

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),    
        }
        labels = {
            'name': 'Nome do cargo',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'registration_number', 'position']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'registration_number': 'Número da matrícula'
        }

    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Cargo ocupado"
    )

class PastaForm(forms.ModelForm):
    class Meta:
        model = Pasta
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),    
        }
        labels = {
            'name': 'Nome da massa',
        }

class StuffingForm(forms.ModelForm):
    class Meta:
        model = Stuffing
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),    
        }
        labels = {
            'name': 'Nome do recheio',
        }

class ProductionDailyRecordForm(forms.ModelForm):
    class Meta:
        model = ProductionDailyRecord
        fields = ['author', 'production_leader', 'date']
        
    author = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Autor do registro"
    )
    production_leader = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Líder de produção"
    )
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
        ),
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        label="Data do registro"
    )

class FinishedPastaForm(forms.ModelForm):
    class Meta:
        model = FinishedPasta
        fields = ['production_record', 'finished_pasta', 'quantity', 'waste']
    finished_pasta = forms.ModelChoiceField(
        queryset=Pasta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Massa acabada",
        required=False
    )
    production_record = forms.ModelChoiceField(
        queryset=ProductionDailyRecord.objects.all().order_by('-date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Registro de produção"
    )
    quantity = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    waste = forms.DecimalField(label='Desperdício', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), required=False)

class InProgressPastaForm(forms.ModelForm):
    class Meta:
        model = InProgressPasta
        fields = ['production_record', 'employee', 'in_progress_pasta', 'quantity']
    in_progress_pasta = forms.ModelChoiceField(
        queryset=Pasta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Massa em elaboração",
        required=False
    )
    employee= forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Colaborador",
        required=False
    )
    production_record = forms.ModelChoiceField(
        queryset=ProductionDailyRecord.objects.all().order_by('-date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Registro de produção"
    )
    quantity = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

class PastaMachineForm(forms.ModelForm):
    class Meta:
        model = PastaMachine
        fields = ['production_record', 'employee', 'machine']
    employee= forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Colaborador",
        required=False
    )
    production_record = forms.ModelChoiceField(
        queryset=ProductionDailyRecord.objects.all().order_by('-date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Registro de produção"
    )
    machine = forms.IntegerField(label='Masseiras', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

class PastaCookingForm(forms.ModelForm):
    class Meta:
        model = PastaCooking
        fields = ['production_record', 'employee', 'pasta_cooking', 'quantity', 'discard']
    employee= forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Colaborador",
        required=False
    )
    production_record = forms.ModelChoiceField(
        queryset=ProductionDailyRecord.objects.all().order_by('-date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Registro de produção"
    )
    pasta_cooking = forms.ModelChoiceField(
        queryset=Pasta.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Massa em cozimento",
        required=False
    )
    quantity = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    discard = forms.DecimalField(label='Descarte', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), required=False)

class PastaStuffingForm(forms.ModelForm):
    class Meta:
        model = PastaStuffing
        fields = ['production_record', 'employee', 'stuffing', 'recipes']
    employee= forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Colaborador",
        required=False
    )
    production_record = forms.ModelChoiceField(
        queryset=ProductionDailyRecord.objects.all().order_by('-date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Registro de produção"
    )
    stuffing = forms.ModelChoiceField(
        queryset=Stuffing.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Recheio",
        required=False
    )
    recipes = forms.IntegerField(label="Receitas", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

#Formsets
FinishedPastaFormSet = inlineformset_factory(
    ProductionDailyRecord,
    FinishedPasta,
    form=FinishedPastaForm,
    extra=7,
    can_delete=False
)
InProgressPastaFormSet = inlineformset_factory(
    ProductionDailyRecord,
    InProgressPasta,
    form=InProgressPastaForm,
    extra=7,
    can_delete=False
)
PastaMachineFormSet = inlineformset_factory(
    ProductionDailyRecord,
    PastaMachine,
    form=PastaMachineForm,
    extra=6,
    can_delete=False
)
PastaCookingFormSet = inlineformset_factory(
    ProductionDailyRecord,
    PastaCooking,
    form=PastaCookingForm,
    extra=6,
    can_delete=False
)
PastaStuffingFormSet = inlineformset_factory(
    ProductionDailyRecord,
    PastaStuffing,
    form=PastaStuffingForm,
    extra=6,
    can_delete=False
)