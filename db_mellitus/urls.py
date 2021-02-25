from django.urls import path

from . import views

urlpatterns = [
    path('diagnose/<int:pk>', views.dm_prediction, name='diagnose-patient'),
    path('patient-list/', views.patient_list, name='patient-list'),
    path('view/<int:pk>', views.patient_view, name='patient-view'),
    path('new/', views.patient_create, name='patient-new'),
    path('edit/<int:pk>', views.patient_update, name='patient-edit'),
    path('delete/<int:pk>', views.patient_delete, name='patient-delete'),
]
