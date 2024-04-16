from django.urls import path
from .views import FileUploadStrategy


urlpatterns = [
    path('upload_file/', FileUploadStrategy.as_view(), name='file_upload_view'),
]
