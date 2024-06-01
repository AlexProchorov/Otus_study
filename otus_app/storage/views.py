import requests
from rest_framework.response import Response
from rest_framework import status
from .models import Storage
from .serializers import StorageSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
def create_storage(request,pk):
    if request.method == 'POST':
        serializer = StorageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

