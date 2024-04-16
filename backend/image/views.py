from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .serializers import FileSerializer
# Create your views here.


class FileUploadThrottle(UserRateThrottle):
    scope = 'sustained'


class FileUploadStrategy(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [FileUploadThrottle] if not settings.DEBUG else []

    def post(self, request):
        serializer = FileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

