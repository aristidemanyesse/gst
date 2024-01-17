from django.forms import ModelForm
from .models import *

        
class NewletterForm(ModelForm):
    class Meta:
        model = Newletter
        fields = "__all__"
        
        
class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"
        