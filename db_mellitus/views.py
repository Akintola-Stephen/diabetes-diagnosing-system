from .forms import RegisterPatientForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Symptom
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
import numpy as np
import joblib

# Create your views here.


@require_http_methods(["GET", "POST"])
def patient_create(request):
    print(request)
    person = Patient()
    person.first_name = request.POST.get('first_name')
    person.middle_name = request.POST.get('middle_name')
    person.last_name = request.POST.get('last_name')
    person.dob = request.POST.get('dob')
    person.gender = request.POST.get('gender')
    person.save()
    return render(request, 'patient/patient-form.html')


def patient_list(request, template_name='patient/patient-list.html'):
    # noinspection PyUnresolvedReferences
    patient = Patient.objects.all()
    paginator = Paginator(patient, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name, {'object_list': patient, 'page_obj': page_obj})


@require_http_methods(["POST", "GET"])
def patient_update(request, pk, template_name='patient/patient-edit.html'):
    person = get_object_or_404(Patient, pk=pk)
    person.first_name = request.POST.get('first_name')
    person.middle_name = request.POST.get('middle_name')
    person.last_name = request.POST.get('last_name')
    person.dob = request.POST.get('dob')
    person.gender = request.POST.get('gender')
    person.save()
    context = {
        'object': person
    }
    return render(request, template_name, {'object': person})


@require_http_methods(["GET", "POST"])
def patient_delete(request, pk, template_name='patient/patient-confirm-delete.html'):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient-list')
    return render(request, template_name, {'object': patient})


def patient_view(request, pk, template_name='patient/patient-detail.html'):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, template_name, {'object': patient})


@require_http_methods(["GET", "POST"])
def dm_prediction(request, pk):
    symptom = get_object_or_404(Patient, pk=pk)
    symptom.pregnancy_count = request.POST.get("pregnancy_count")
    symptom.plasma = request.POST.get("plasma")
    symptom.blood_pressure = request.POST.get("blood_pressure")
    symptom.skin_thickness = request.POST.get("skin_thickness")
    symptom.insulin = request.POST.get("insulin")
    symptom.bmi = request.POST.get("bmi")
    symptom.pedigree = request.POST.get("pedigree")
    symptom.age = request.POST.get("age")

    user_data = np.array(
        [
            [
                symptom.pregnancy_count, symptom.plasma,
                symptom.blood_pressure, symptom.skin_thickness,
                symptom.insulin, symptom.bmi,
                symptom.pedigree, symptom.age
            ]
        ]
    ).reshape(1, 8)

    model_path = 'ml_model/model.pkl'
    svc = joblib.load(open(model_path, 'rb'))
    prediction = svc.predict(user_data)

    symptom.prediction_result = prediction[0]
    symptom.save()

    context = {
        'patient': symptom
    }

    return render(request, "patient/diagnose.html", context)
