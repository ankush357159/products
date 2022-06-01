from django import forms
from store.models import MyModel

class MyForm(forms.ModelForm):

    class Meta:
        model = MyModel
        
        fields = ["title", "description"]