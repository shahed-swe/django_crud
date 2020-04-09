from django.contrib import admin
from crud.models import Information
# Register your models here.
admin.site.register(Information)
admin.site.site_header = "My Administratoin"