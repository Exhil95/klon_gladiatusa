from django import forms
from .models import UserProfile

class RozdielPktStatystyk(forms.ModelForm):
    strength = forms.IntegerField(min_value=0, required=False, label="Siła")
    dexterity = forms.IntegerField(min_value=0, required=False, label="Zręczność")
    constitution = forms.IntegerField(min_value=0, required=False, label="Kondycja")
    intelligence = forms.IntegerField(min_value=0, required=False, label="Inteligencja")
    
    class Meta:
        model = UserProfile
        fields = ['strength', 'dexterity', 'constitution', 'intelligence']
        
    def clean(self):
        cleaned_data = super().clean()
        pkt = sum(filter(None, cleaned_data.values()))
        if pkt > self.instance.stat_points:
            raise forms.ValidationError("Nie masz tylu punktów do rozdania")
        return cleaned_data