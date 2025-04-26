from rest_framework import generics
from .models import (Position, Employee, Pasta, Stuffing, ProductionDailyRecord, 
                     FinishedPasta, InProgressPasta, PastaMachine, PastaCooking, PastaStuffing)
from .serializers import (
    GetEmployeeSerializer, PositionSerializer, EmployeeSerializer, PastaSerializer, ProductionDailyRecordCompleteSerializer, ProductionDailyRecordsCompleteSerializer, ProductionDailyRecordsSerializer, RegistrationNumberSerializer, StuffingSerializer, ProductionDailyRecordSerializer,
    FinishedPastaSerializer, InProgressPastaSerializer, PastaMachineSerializer, PastaCookingSerializer, PastaStuffingSerializer
)

# Endpoints para Position
class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

# Endpoints para Employee
class EmployeeListAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = GetEmployeeSerializer
    
class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = GetEmployeeSerializer
    

# Endpoints para Employee
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class RegistrationNumberListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = RegistrationNumberSerializer

# Endpoints para Pasta
class PastaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pasta.objects.all()
    serializer_class = PastaSerializer

class PastaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pasta.objects.all()
    serializer_class = PastaSerializer

# Endpoints para Stuffing
class StuffingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stuffing.objects.all()
    serializer_class = StuffingSerializer

class StuffingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stuffing.objects.all()
    serializer_class = StuffingSerializer

# Endpoints para ProductionDailyRecords
class ProductionDailyRecordsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordsSerializer

class ProductionDailyRecordsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordsSerializer
  
  
    
class ProductionDailyRecordsCompleteListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordsCompleteSerializer

class ProductionDailyRecordsCompleteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordsCompleteSerializer    

# Endpoints para ProductionDailyRecord
class ProductionDailyRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordSerializer

class ProductionDailyRecordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordSerializer
    
class ProductionDailyRecordCompleteListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordCompleteSerializer

class ProductionDailyRecordCompleteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionDailyRecord.objects.all()
    serializer_class = ProductionDailyRecordCompleteSerializer    



# Endpoints para FinishedPasta
class FinishedPastaListCreateAPIView(generics.ListCreateAPIView):
    queryset = FinishedPasta.objects.all()
    serializer_class = FinishedPastaSerializer

class FinishedPastaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinishedPasta.objects.all()
    serializer_class = FinishedPastaSerializer

# Endpoints para InProgressPasta
class InProgressPastaListCreateAPIView(generics.ListCreateAPIView):
    queryset = InProgressPasta.objects.all()
    serializer_class = InProgressPastaSerializer

class InProgressPastaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InProgressPasta.objects.all()
    serializer_class = InProgressPastaSerializer

# Endpoints para PastaMachine
class PastaMachineListCreateAPIView(generics.ListCreateAPIView):
    queryset = PastaMachine.objects.all()
    serializer_class = PastaMachineSerializer

class PastaMachineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastaMachine.objects.all()
    serializer_class = PastaMachineSerializer

# Endpoints para PastaCooking
class PastaCookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = PastaCooking.objects.all()
    serializer_class = PastaCookingSerializer

class PastaCookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastaCooking.objects.all()
    serializer_class = PastaCookingSerializer

# Endpoints para PastaStuffing
class PastaStuffingListCreateAPIView(generics.ListCreateAPIView):
    queryset = PastaStuffing.objects.all()
    serializer_class = PastaStuffingSerializer

class PastaStuffingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastaStuffing.objects.all()
    serializer_class = PastaStuffingSerializer
