from django import forms

from .models import Delivery

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = (
            'city',
            'address',
            'house',
            'apartment',
            'payment',
            'comment'
        )
    
    def save(self, commit: bool = ...) -> Delivery:
        self.full_clean()
        return super().save(commit)