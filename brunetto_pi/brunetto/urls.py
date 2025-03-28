from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'), 
  
    # CRUD de Posições
    path('position/create/', views.create_position, name='create_position'),
    path('positions', views.read_positions, name='read_positions'),
    path('position/update/<int:pk>/', views.update_position, name='update_position'),
    path('position/delete/<int:pk>/', views.delete_position, name='delete_position'),

    # CRUD de Colaboradores
    path('employee/create/', views.create_employee, name='create_employee'),
    path('employees', views.read_employees, name='read_employees'),
    path('employee/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employee/delete/<int:pk>/', views.delete_employee, name='delete_employee'),

    # CRUD de Massas
    path('pasta/create/', views.create_pasta, name='create_pasta'),
    path('pastas', views.read_pastas, name='read_pastas'),
    path('pasta/update/<int:pk>/', views.update_pasta, name='update_pasta'),
    path('pasta/delete/<int:pk>/', views.delete_pasta, name='delete_pasta'),

    # CRUD de Recheios
    path('stuffing/create/', views.create_stuffing, name='create_stuffing'),
    path('stuffings', views.read_stuffings, name='read_stuffings'),
    path('stuffing/update/<int:pk>/', views.update_stuffing, name='update_stuffing'),
    path('stuffing/delete/<int:pk>/', views.delete_stuffing, name='delete_stuffing'),

    # CRUD de Registro diário de produção
    path('production_daily_record/create/', views.create_production_daily_record, name='create_production_daily_record'),
    path('production_daily_record/<int:pk>/', views.read_production_daily_record, name='read_production_daily_record'),
    path('production_daily_records/', views.list_production_daily_records, name='list_production_daily_records'),
    path('production_daily_record/update/<int:pk>/', views.update_production_daily_record, name='update_production_daily_record'),
    path('production_daily_record/delete/<int:pk>/', views.delete_production_daily_record, name='delete_production_daily_record'),
    
]