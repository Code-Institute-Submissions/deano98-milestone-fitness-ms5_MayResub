from django import forms

class WeightForm(forms.Form):
    ''' Total daily energy expenditure form '''

    current_weight = forms.IntegerField(required=True)
