from pypdf import PdfReader
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from api.model.gemini.main import get_extracted_content_from_file, fine_tuning_extracted_contents_from_file
from .models import File


@receiver(post_save, sender=File)
def post_save(sender, instance, **kwargs):

    if not instance or hasattr(instance, '_dirty'):
        return

    # Checking if content already exists then using it otherwise extracting contents from the file
    if instance.content != '':
        content = instance.content
    else:
        content = ''
        reader = PdfReader(instance.file)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            content = content + '\n' + page.extract_text()

    # Extracting the rules content from the file
    if instance.content_extracted != '':
        content_extracted = instance.content_extracted
        print('Inside using already content')
    else:
        content_extracted = get_extracted_content_from_file(content)
        print('Inside generating text extraction')

    # Checking the fine tuning text if any any accordingly manipulating the rules
    fine_tuned_content = None
    if instance.fine_tuning_text != '':
        fine_tuned_content = fine_tuning_extracted_contents_from_file(text=content_extracted,
                                                                      fine_tuning_prompt=instance.fine_tuning_text)

    try:
        instance._dirty = True
        instance.content = content
        instance.content_extracted = content_extracted if fine_tuned_content is None else fine_tuned_content
        instance.fine_tuning_text = ''
        instance.save()
    finally:
        del instance._dirty
