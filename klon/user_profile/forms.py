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
        print(f"Wyczyszczone dane: {cleaned_data}")
        pkt = sum(filter(None, cleaned_data.values()))
        print(f"Suma rozdanych pkt: {pkt}")
        print(f"Pkt możliwe do rozdania: {self.instance.stat_points}")
        if pkt > self.instance.stat_points:
            raise forms.ValidationError("Nie masz tylu punktów do rozdania")
        for field, value in cleaned_data.items():
            if value < 0:
                raise forms.ValidationError("Nie można odejmować punktów")
        return cleaned_data