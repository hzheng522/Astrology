from django import forms

class BirthChartForm(forms.Form):
    name = forms.CharField(required=False)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birth_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    timezone = forms.FloatField()