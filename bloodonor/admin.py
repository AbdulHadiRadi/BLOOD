from django.contrib import admin
from api.models import Account, Donor,Request
# Register your models here.
admin.register(Account)
admin.register(Request)
admin.register(Donor)