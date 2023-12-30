from django.contrib import admin
from .models import GeeksModel
from .models import ContactsModel
from .models import PaymentsModel1
from .models import LoginModel
# Register your models here.

admin.site.register(PaymentsModel1,),
admin.site.register(GeeksModel,),
admin.site.register(ContactsModel,),
admin.site.register(LoginModel,),

