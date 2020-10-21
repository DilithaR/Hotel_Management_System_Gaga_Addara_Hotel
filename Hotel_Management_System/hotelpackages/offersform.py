from django import forms  

from hotelpackages.models import Offers

class OffersForm(forms.ModelForm):  
    class Meta:  
        model = Offers  
        fields = "__all__"  


