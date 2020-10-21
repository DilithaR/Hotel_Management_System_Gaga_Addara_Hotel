from django import forms  

from hotelpackages.models import Packages

class PackageForm(forms.ModelForm):  
    class Meta:  
        model = Packages  
        fields = "__all__"  


