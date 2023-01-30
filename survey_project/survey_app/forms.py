from django import forms

from .models import ElectionSurveyDetails

class SurveyForm(forms.ModelForm):

    class Meta:
        model = ElectionSurveyDetails
        fields = '__all__'