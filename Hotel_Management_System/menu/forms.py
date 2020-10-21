from django.forms import ModelForm
from .models import Project
from promotions.models import Promo

class MenuBackendForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image','price']


class promoBackendForm(ModelForm):
    class Meta:
        model = Promo
        fields = ['promoTitle','promoDescription','promoImage','promoPrice','expiredate']
