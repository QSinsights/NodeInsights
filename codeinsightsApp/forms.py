from django import forms
from .models import VS1H1

class VS2H1(forms.ModelForm):
    class Meta:
        model = VS1H1
        fields = ['Log_Time',
    'Stakeholder_Name',
    'Wake_up_time',
    'Caffiene_Intake',
    'Exercise_Description',
    'Routine_Description',
    'Review_Intentions',
    'Intended_Methods',
    'Session_Duration',
    'Integrate_Awakening',]
