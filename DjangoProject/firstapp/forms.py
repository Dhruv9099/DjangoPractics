from django import forms
from .models import scriptingLang

class ScriptVarietyForm(forms.Form):
    script_variety = forms.ModelChoiceField(queryset=scriptingLang.objects.all(),label="Select script variety")