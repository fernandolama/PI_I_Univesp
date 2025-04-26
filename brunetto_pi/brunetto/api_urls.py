from django.urls import path
from .api_views import (
    EmployeeListAPIView, EmployeeRetrieveAPIView, PositionListCreateAPIView, PositionRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView,
    PastaListCreateAPIView, PastaRetrieveUpdateDestroyAPIView, ProductionDailyRecordCompleteListCreateAPIView, ProductionDailyRecordCompleteRetrieveUpdateDestroyAPIView, ProductionDailyRecordsCompleteListCreateAPIView, ProductionDailyRecordsCompleteRetrieveUpdateDestroyAPIView, ProductionDailyRecordsListCreateAPIView, ProductionDailyRecordsRetrieveUpdateDestroyAPIView, RegistrationNumberListAPIView,
    StuffingListCreateAPIView, StuffingRetrieveUpdateDestroyAPIView,
    ProductionDailyRecordListCreateAPIView, ProductionDailyRecordRetrieveUpdateDestroyAPIView,
    FinishedPastaListCreateAPIView, FinishedPastaRetrieveUpdateDestroyAPIView,
    InProgressPastaListCreateAPIView, InProgressPastaRetrieveUpdateDestroyAPIView,
    PastaMachineListCreateAPIView, PastaMachineRetrieveUpdateDestroyAPIView,
    PastaCookingListCreateAPIView, PastaCookingRetrieveUpdateDestroyAPIView,
    PastaStuffingListCreateAPIView, PastaStuffingRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Endpoints para Position
    path('positions/', PositionListCreateAPIView.as_view(), name='positions-list-create'),
    path('positions/<int:pk>/', PositionRetrieveUpdateDestroyAPIView.as_view(), name='positions-detail'),

    # Endpoints para Employee
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employees-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employees-detail'),
    # path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employees-detail'),

    path('employees/get/', EmployeeListAPIView.as_view(), name='employees-list'),
    path('employees/get/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employees-detail'),
    
    path('employees/get/registration_number/', RegistrationNumberListAPIView.as_view(), name='registrarion-number-list'),    

    # Endpoints para Pasta
    path('pastas/', PastaListCreateAPIView.as_view(), name='pastas-list-create'),
    path('pastas/<int:pk>/', PastaRetrieveUpdateDestroyAPIView.as_view(), name='pastas-detail'),

    # Endpoints para Stuffing
    path('stuffings/', StuffingListCreateAPIView.as_view(), name='stuffings-list-create'),
    path('stuffings/<int:pk>/', StuffingRetrieveUpdateDestroyAPIView.as_view(), name='stuffings-detail'),

    # Endpoints para ProductionDailyRecord
    path('production-daily-records/', ProductionDailyRecordsListCreateAPIView.as_view(), name='production-daily-records-list-create'),
    path('production-daily-records/<int:pk>/', ProductionDailyRecordsRetrieveUpdateDestroyAPIView.as_view(), name='production-daily-records-detail'),
    
    path('production-daily-records-complete/', ProductionDailyRecordsCompleteListCreateAPIView.as_view(), name='production-daily-records-complete-list-create'),
    path('production-daily-records-complete/<int:pk>/', ProductionDailyRecordsCompleteRetrieveUpdateDestroyAPIView.as_view(), name='production-daily-records-complete-detail'),
    
    # Endpoints para ProductionDailyRecord
    path('production-daily-record/', ProductionDailyRecordListCreateAPIView.as_view(), name='production-daily-record-list-create'),
    path('production-daily-record/<int:pk>/', ProductionDailyRecordRetrieveUpdateDestroyAPIView.as_view(), name='production-daily-record-detail'),
    
    path('production-daily-record-complete/', ProductionDailyRecordCompleteListCreateAPIView.as_view(), name='production-daily-record-complete-list-create'),
    path('production-daily-record-complete/<int:pk>/', ProductionDailyRecordCompleteRetrieveUpdateDestroyAPIView.as_view(), name='production-daily-record-complete-detail'),
    


    # Endpoints para FinishedPasta
    path('finished-pastas/', FinishedPastaListCreateAPIView.as_view(), name='finished-pastas-list-create'),
    path('finished-pastas/<int:pk>/', FinishedPastaRetrieveUpdateDestroyAPIView.as_view(), name='finished-pastas-detail'),

    # Endpoints para InProgressPasta
    path('in-progress-pastas/', InProgressPastaListCreateAPIView.as_view(), name='in-progress-pastas-list-create'),
    path('in-progress-pastas/<int:pk>/', InProgressPastaRetrieveUpdateDestroyAPIView.as_view(), name='in-progress-pastas-detail'),

    # Endpoints para PastaMachine
    path('pasta-machines/', PastaMachineListCreateAPIView.as_view(), name='pasta-machines-list-create'),
    path('pasta-machines/<int:pk>/', PastaMachineRetrieveUpdateDestroyAPIView.as_view(), name='pasta-machines-detail'),

    # Endpoints para PastaCooking
    path('pasta-cookings/', PastaCookingListCreateAPIView.as_view(), name='pasta-cookings-list-create'),
    path('pasta-cookings/<int:pk>/', PastaCookingRetrieveUpdateDestroyAPIView.as_view(), name='pasta-cookings-detail'),

    # Endpoints para PastaStuffing
    path('pasta-stuffings/', PastaStuffingListCreateAPIView.as_view(), name='pasta-stuffings-list-create'),
    path('pasta-stuffings/<int:pk>/', PastaStuffingRetrieveUpdateDestroyAPIView.as_view(), name='pasta-stuffings-detail'),
]
