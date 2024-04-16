from rest_framework import serializers
from pypdf import PdfReader
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # reader = PdfReader(validated_data['file'])
        # page = reader.pages[0]
        # validated_data['content'] = page.extract_text()

        return File.objects.create(**validated_data)
