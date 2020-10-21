from django import forms
from feedback_app.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        managed = False
        model = Feedback
        fields = ('category','description',)
        
class AnswerForm(forms.ModelForm):
    class Meta:
        managed = False
        model = Feedback
        fields = ('ansDescription',)

        
        #"_all_"