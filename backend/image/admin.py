from django.contrib import admin
from .models import File, FileAdmin


# Register your models here.
admin.site.register(File, FileAdmin)
