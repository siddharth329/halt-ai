from django.contrib import admin
from .models import LLMQuery, LLMQueryAdmin


# Register your models here.
admin.site.register(LLMQuery, LLMQueryAdmin)
