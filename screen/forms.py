from django import forms
from .models import Level


class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['level', 'image']

        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }