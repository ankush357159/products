from django import forms
from bunny.models import MyPet
from django.forms import TextInput, NumberInput, FileInput


class MyPetForm(forms.ModelForm):
    class Meta:
        model = MyPet
        fields = ['name', 'age', 'breed', 'color', 'weight', 'photo']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Pet Name',                
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Age'
            }),
             'breed': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Breed'
            }),
             'color': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Color'
            }),
               'weight': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Weight'
            }),
               'photo': FileInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Choose pic to upload'
            }),

        }