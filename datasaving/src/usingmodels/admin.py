from django.contrib import admin
from .models import cust_details, personal_details
# Register your models here.
admin.site.register(cust_details)
admin.site.register(personal_details)