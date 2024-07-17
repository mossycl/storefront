from django.contrib import admin

from .models import Comuna, Region, Usuario

# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Usuario)