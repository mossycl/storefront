from django.contrib import admin

from .models import Comuna, Region, Cliente

# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Cliente)