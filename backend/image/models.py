from django.db import models
from django.contrib.admin import ModelAdmin
from django.forms import Textarea
# Create your models here.

TEMP = 'TEMPORARY'
PERM = 'PERMANENT'


def file_location(instance, filename):
    return f'files/{filename}.pdf'


class File(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    content = models.TextField(default='', blank=True, null=True)
    content_extracted = models.TextField(default='', blank=True, null=True)
    fine_tuning_text = models.TextField(default='', blank=True, null=True)
    file = models.FileField(upload_to=file_location)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'File-{self.id}'


class FileAdmin(ModelAdmin):
    search_fields = ('title', )
    ordering = ('-created_at', )
    list_filter = ('active', )
    list_display = ('id', 'title', 'active', 'created_at', 'file')
    fieldsets = (
        ('Required', {'fields': ('title', 'file', 'active'),
                      'description': """
                      <strong>Note</strong>: <br>
                      When creating a file, only the following fields need to be set. <br>
                      Fine tuning prompt is optional and will be applied to the extracted content. <br>
                      Content extracted can be modified manually if required. <br>
                      Only the rules from active files will be chosen to check the user queries. <br>
                      """}),
        ('Fine Tuning', {'fields': ('fine_tuning_text', )}),
        ('Contents - (Automated)', {'fields': ('content', 'content_extracted')}),
        ('Metrics', {'fields': ('created_at', 'updated_at')})
    )
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }
