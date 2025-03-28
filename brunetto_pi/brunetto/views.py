from django.shortcuts import render, redirect,  get_object_or_404
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

# CRUD Position
def create_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_positions')
    else:
        form = PositionForm()
    return render(request, 'create_position.html', {'form': form})

def read_positions(request):
    order_by = request.GET.get('order_by', 'name')
    if order_by.startswith('-'):
        new_order_by = order_by[1:]
    else:
        new_order_by = f'-{order_by}'
    positions = Position.objects.all().order_by(order_by)
    return render(request, 'read_positions.html', {
        'positions': positions,
        'current_order': order_by,
        'new_order': new_order_by
    })

def update_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        
        if form.is_valid():
            form.save()
            return redirect('read_positions')
    
    else:
        form = PositionForm(instance=position)
    
    return render(request, 'update_position.html', {
        'form': form,
        'position': position,
    })

def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('read_positions')
    return render(request, 'delete.html', {'object': position, 'type': 'Posição'})

# CRUD Emmployee
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_employees')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def read_employees(request):
    order_by = request.GET.get('order_by', 'name')
    if order_by.startswith('-'):
        new_order_by = order_by[1:]
    else:
        new_order_by = f'-{order_by}'
    employees = Employee.objects.all().order_by(order_by)
    return render(request, 'read_employees.html', {
        'employees': employees,
        'current_order': order_by,
        'new_order': new_order_by
    })

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('read_employees')
    
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'update_employee.html', {
        'form': form,
        'employee': employee,
    })

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('read_employees')
    return render(request, 'delete.html', {'object': employee, 'type': 'Colaborador'})

# CRUD Pasta
def create_pasta(request):
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_pastas')
    else:
        form = PastaForm()
    return render(request, 'create_pasta.html', {'form': form})

def read_pastas(request):
    order_by = request.GET.get('order_by', 'name')
    if order_by.startswith('-'):
        new_order_by = order_by[1:]
    else:
        new_order_by = f'-{order_by}'
    pastas = Pasta.objects.all().order_by(order_by)
    return render(request, 'read_pastas.html', {
        'pastas': pastas,
        'current_order': order_by,
        'new_order': new_order_by
    })

def update_pasta(request, pk):
    pasta = get_object_or_404(Pasta, pk=pk)
    
    if request.method == 'POST':
        form = PastaForm(request.POST, instance=pasta)
        
        if form.is_valid():
            form.save()
            return redirect('read_pastas')
    
    else:
        form = PastaForm(instance=pasta)
    
    return render(request, 'update_pasta.html', {
        'form': form,
        'position': pasta,
    })

def delete_pasta(request, pk):
    pasta = get_object_or_404(Pasta, pk=pk)
    if request.method == 'POST':
        pasta.delete()
        return redirect('read_pastas')
    return render(request, 'delete.html', {'object': pasta, 'type': 'Massa'})

# CRUD Stuffing
def create_stuffing(request):
    if request.method == 'POST':
        form = StuffingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_stuffings')
    else:
        form = PastaForm()
    return render(request, 'create_stuffing.html', {'form': form})

def read_stuffings(request):
    order_by = request.GET.get('order_by', 'name')
    if order_by.startswith('-'):
        new_order_by = order_by[1:]
    else:
        new_order_by = f'-{order_by}'
    stuffings = Stuffing.objects.all().order_by(order_by)
    return render(request, 'read_stuffings.html', {
        'stuffings': stuffings,
        'current_order': order_by,
        'new_order': new_order_by
    })

def update_stuffing(request, pk):
    stuffing = get_object_or_404(Pasta, pk=pk)
    
    if request.method == 'POST':
        form = StuffingForm(request.POST, instance=stuffing)
        
        if form.is_valid():
            form.save()
            return redirect('read_stuffings')
    
    else:
        form = StuffingForm(instance=stuffing)
    
    return render(request, 'update_stuffing.html', {
        'form': form,
        'position': stuffing,
    })

def delete_stuffing(request, pk):
    stuffing = get_object_or_404(Stuffing, pk=pk)
    if request.method == 'POST':
        stuffing.delete()
        return redirect('read_stuffings')
    return render(request, 'delete.html', {'object': stuffing, 'type': 'Recheio'})

# CRUD ProductionDailyRecord
def create_production_daily_record(request):
    if request.method == "POST":
        form = ProductionDailyRecordForm(request.POST)
        finished_pasta_formset = FinishedPastaFormSet(request.POST, queryset=FinishedPasta.objects.none())
        in_progress_pasta_formset = InProgressPastaFormSet(request.POST, queryset=InProgressPasta.objects.none())
        pasta_machine_formset = PastaMachineFormSet(request.POST, queryset=PastaMachine.objects.none())
        pasta_cooking_formset = PastaCookingFormSet(request.POST, queryset=PastaCooking.objects.none())
        pasta_stuffing_formset = PastaStuffingFormSet(request.POST, queryset=PastaStuffing.objects.none())

        if form.is_valid() and finished_pasta_formset.is_valid() and in_progress_pasta_formset.is_valid() and pasta_machine_formset.is_valid() and pasta_cooking_formset.is_valid() and pasta_stuffing_formset.is_valid():
            production_record = form.save()
            
            finished_pastas = finished_pasta_formset.save(commit=False)
            for pasta in finished_pastas:
                if pasta.finished_pasta:
                    pasta.production_record = production_record
                    pasta.save()
            
            in_progress_pastas = in_progress_pasta_formset.save(commit=False)
            for pasta in in_progress_pastas:
                if pasta.in_progress_pasta:
                    pasta.production_record = production_record
                    pasta.save()

            pasta_machine_usages = pasta_machine_formset.save(commit=False)
            for usage in pasta_machine_usages:
                if usage.machine:
                    usage.production_record = production_record
                    usage.save()

            cooking_pastas = pasta_cooking_formset.save(commit=False)
            for pasta in cooking_pastas:
                if pasta.pasta_cooking:
                    pasta.production_record = production_record
                    pasta.save()

            pasta_stuffings = pasta_stuffing_formset.save(commit=False)
            for stuffing in pasta_stuffings:
                if stuffing.stuffing:
                    stuffing.production_record = production_record
                    stuffing.save()

            return redirect("list_production_daily_records")

    else:
        form = ProductionDailyRecordForm()
        finished_pasta_formset = FinishedPastaFormSet(queryset=FinishedPasta.objects.none())
        in_progress_pasta_formset = InProgressPastaFormSet(queryset=InProgressPasta.objects.none())
        pasta_machine_formset = PastaMachineFormSet(queryset=PastaMachine.objects.none())
        pasta_cooking_formset = PastaCookingFormSet(queryset=PastaCooking.objects.none())
        pasta_stuffing_formset = PastaStuffingFormSet(queryset=PastaStuffing.objects.none())

    return render(request, "create_production_daily_record.html", {
        "form": form,
        "finished_pasta_formset": finished_pasta_formset,
        'in_progress_pasta_formset': in_progress_pasta_formset,
        'pasta_machine_formset': pasta_machine_formset,
        'pasta_cooking_formset': pasta_cooking_formset,
        'pasta_stuffing_formset': pasta_stuffing_formset
    })

def read_production_daily_record(request, pk):
    production_record = get_object_or_404(ProductionDailyRecord, pk=pk)
    finished_pasta_formset = FinishedPastaFormSet(instance=production_record)
    in_progress_pasta_formset = InProgressPastaFormSet(instance=production_record)
    pasta_machine_formset = PastaMachineFormSet(instance=production_record)
    pasta_cooking_formset = PastaCookingFormSet(instance=production_record)
    pasta_stuffing_formset = PastaStuffingFormSet(instance=production_record)

    return render(request, 'read_production_daily_record.html', {
        'production_record': production_record,
        'finished_pasta_formset': finished_pasta_formset,
        'in_progress_pasta_formset': in_progress_pasta_formset,
        'pasta_machine_formset': pasta_machine_formset,
        'pasta_cooking_formset': pasta_cooking_formset,
        'pasta_stuffing_formset': pasta_stuffing_formset,
    })

def list_production_daily_records(request):
    records = ProductionDailyRecord.objects.all().order_by('-date')
    return render(request, 'list_production_daily_records.html', {'records': records})

def update_production_daily_record(request, pk):
    production_record = get_object_or_404(ProductionDailyRecord, pk=pk)

    if request.method == "POST":
        form = ProductionDailyRecordForm(request.POST, instance=production_record)
        finished_pasta_formset = FinishedPastaFormSet(request.POST, instance=production_record)
        in_progress_pasta_formset = InProgressPastaFormSet(request.POST, instance=production_record)
        pasta_machine_formset = PastaMachineFormSet(request.POST, instance=production_record)
        pasta_cooking_formset = PastaCookingFormSet(request.POST, instance=production_record)
        pasta_stuffing_formset = PastaStuffingFormSet(request.POST, instance=production_record)

        if form.is_valid() and finished_pasta_formset.is_valid() and in_progress_pasta_formset.is_valid() and pasta_machine_formset.is_valid() and pasta_cooking_formset.is_valid() and pasta_stuffing_formset.is_valid():
            form.save()
            
            finished_pasta_formset.save()
            in_progress_pasta_formset.save()
            pasta_machine_formset.save()
            pasta_cooking_formset.save()
            pasta_stuffing_formset.save()

            return redirect('read_production_daily_record', pk=pk)

    else:
        form = ProductionDailyRecordForm(instance=production_record)
        finished_pasta_formset = FinishedPastaFormSet(instance=production_record, queryset=FinishedPasta.objects.filter(production_record=production_record))
        in_progress_pasta_formset = InProgressPastaFormSet(instance=production_record, queryset=InProgressPasta.objects.filter(production_record=production_record))
        pasta_machine_formset = PastaMachineFormSet(instance=production_record, queryset=PastaMachine.objects.filter(production_record=production_record))
        pasta_cooking_formset = PastaCookingFormSet(instance=production_record, queryset=PastaCooking.objects.filter(production_record=production_record))
        pasta_stuffing_formset = PastaStuffingFormSet(instance=production_record, queryset=PastaStuffing.objects.filter(production_record=production_record))

    return render(request, 'update_production_daily_record.html', {
        'form': form,
        'finished_pasta_formset': finished_pasta_formset,
        'in_progress_pasta_formset': in_progress_pasta_formset,
        'pasta_machine_formset': pasta_machine_formset,
        'pasta_cooking_formset': pasta_cooking_formset,
        'pasta_stuffing_formset': pasta_stuffing_formset,
    })

def delete_production_daily_record(request, pk):
    production_daily_record = get_object_or_404(ProductionDailyRecord, pk=pk)
    if request.method == 'POST':
        production_daily_record.delete()
        return redirect('list_production_daily_records')
    return render(request, 'delete.html', {'object': production_daily_record, 'type': 'Registro Diário de Produção'})
