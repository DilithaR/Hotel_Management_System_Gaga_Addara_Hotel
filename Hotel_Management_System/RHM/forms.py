from django import forms
from RHM.models import ReceptionHallPackage
from RHM.models import ReceptionHallBook 
class ReceptionHallPackageForm(forms.ModelForm):
    class Meta:
        managed = False
        model = ReceptionHallPackage
        fields =  "__all__" 



class ReceptionHallBookForm(forms.ModelForm):
    class Meta:
        managed = False
        model = ReceptionHallBook
        fields = "__all__" 

