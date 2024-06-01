import requests
from rest_framework.response import Response
from rest_framework import status
from .models import Orders
from .serializers import OrderSerializer
from rest_framework.decorators import api_view, permission_classes
from billing.views import payfororder
from django.db import transaction
from django.db.utils import IntegrityError, DatabaseError
from django.http import HttpResponse
from storage.models import Storage


@api_view(['POST'])
def create_order(request,pk):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            request.POST._mutable = True


            with transaction.atomic():
                        # Atomic transaction
                try:
                        sid = transaction.savepoint()
                        Storage.objects.create(Product_id= request.data['Product_id'] , Counts_product= request.data['Counts_product'], Is_booking= True ,User_id =  request.data['UserID'] )
                        # In worst case scenario, this might fail too
                        transaction.savepoint_commit(sid)
                except IntegrityError:
                     transaction.savepoint_rollback(sid)
                        # Non-atomic transaction
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Duplicates should be prevented.