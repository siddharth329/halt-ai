from django.db import models
from django.contrib.admin import ModelAdmin


# Create your models here.
class LLMQuery(models.Model):
    MONITORED_SOURCES = [
        (0, 'CHAT_GPT'),
        (1, 'GEMINI'),
    ]

    ACTION_CHOICES = [
        (0, 'CLEAR'),
        (1, 'WARNING'),
        (2, 'DATA_LEAK')
    ]

    machine_id = models.CharField(max_length=100)
    content = models.TextField()
    source = models.IntegerField(choices=MONITORED_SOURCES)
    blocked = models.BooleanField(default=False)
    error = models.TextField(default='')

    action_required = models.BooleanField(default=False, null=True)
    action_level = models.IntegerField(default=0, null=True, choices=ACTION_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.content}'


class LLMQueryAdmin(ModelAdmin):
    search_fields = ('machine_id', )
    ordering = ('-created_at', )
    list_filter = ('blocked', 'action_required', 'action_level')
    list_display = ('id', 'machine_id', 'source', 'blocked', 'action_required', 'action_level', 'created_at')
    fieldsets = (
        ('Required', {'fields': ('machine_id', 'content', 'source')}),
        ('LLM Response', {'fields': ('blocked', 'error')}),
        ('Admin Assist', {'fields': ('action_required', 'action_level')}),
        ('Metrics', {'fields': ('created_at', 'updated_at')})
    )
    readonly_fields = ('created_at', 'updated_at')
