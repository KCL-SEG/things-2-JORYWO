"""Forms of the project."""

# Create your forms here.
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label="Name")
    description = forms.TextArea(label="Description")
    quantity = forms.NumberInput(label="")

