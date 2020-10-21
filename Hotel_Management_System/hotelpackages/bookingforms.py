from django import forms  
from hotelpackages.models import Booking


class BookingForm(forms.ModelForm):  
    class Meta:  
        model = Booking  
        fields = "__all__"  


