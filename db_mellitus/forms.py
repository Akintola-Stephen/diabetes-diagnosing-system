from django import formsfrom .models import  Patient, Symptomclass RegisterPatientForm(forms.ModelForm):    class Meta:        model = Patient        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'gender', )        #exclude = ( '__symptom__',)class SymptomForm(forms.ModelForm):    class Meta:        model = Symptom        fields = '__all__'