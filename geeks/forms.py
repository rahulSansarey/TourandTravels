from django import forms
from .models import GeeksModel
from .models import ContactsModel
from .models import LoginModel


class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = ["title","description","arrival",]
    
class ContactsForm(forms.ModelForm):
    class Meta:
        model = ContactsModel
        fields = ["name","email","number","subject","message",]

class LoginModel(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ["name","email","password"]

##class PaymentsForm(forms.ModelForm):
##    class Meta:
##        model = PaymentsModel
##        fields = ["fullname","email","address","city","state"
##                  "zipcode","nameoncard","cardnumber",
##                  "exp.month","exp.year","cvv",]        
##    
