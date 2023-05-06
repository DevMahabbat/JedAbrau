


from django import forms

from app.models import Muraciet

class MuracietForm(forms.ModelForm):
    
    class Meta:
        model = Muraciet
        fields = ("ad","soyad","telefon","email","qeyd")
