from django import forms
from .models import UserProfile

class RozdielPktStatystyk(forms.ModelForm):
    """
    Formularz dla rozdzielenia pkt statystyk.
    """
    strength = forms.IntegerField(min_value=0, required=False, label="Siła")
    dexterity = forms.IntegerField(min_value=0, required=False, label="Zręczność")
    constitution = forms.IntegerField(min_value=0, required=False, label="Kondycja")
    intelligence = forms.IntegerField(min_value=0, required=False, label="Inteligencja")
    
    class Meta:
        model = UserProfile
        fields = ['strength', 'dexterity', 'constitution', 'intelligence']
        
    def clean(self):
        """
        Walidacja danych z formularza.
        """
        cleaned_data = super().clean()
        pkt = 0
        for field in ['strength', 'dexterity', 'constitution', 'intelligence']:
            value = cleaned_data.get(field)
            base_value = getattr(self.instance, f'base_{field}', 0)
            if value is not None:
                if value < base_value:
                    raise forms.ValidationError("Nie można odejmować punktów.")
                pkt += value - base_value
        if pkt > self.instance.stat_points:
            raise forms.ValidationError("Nie masz tylu punktów do rozdania.")
        return cleaned_data