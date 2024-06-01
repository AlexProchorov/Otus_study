
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BillingSerializer
from .models import Billing
from order.models import Orders
from order.serializers import OrderSerializer



@api_view(['POST'])
def depositmoney(request,pk):
    if request.method == 'POST':
        user = Billing.objects.get(pk=pk)
        before_adding = Billing.objects.get(pk=pk).SumCount
        request.POST._mutable = True
        a = request.data['SumCount']
        request.data['SumCount'] = before_adding + a
        request.data['Message'] = 'Баланс пополнен успешно'
        serializer = BillingSerializer(instance=user, data=request.data)


        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def withdrawmoney(request,pk):
    if request.method == 'POST':
        user = Billing.objects.get(pk=pk)
        before_adding = Billing.objects.get(pk=pk).SumCount
        request.POST._mutable = True
        a = request.data['SumCount']
        if before_adding - a >= 0:
            request.data['SumCount'] = before_adding - a
            serializer = BillingSerializer(instance=user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Недостаточно средств', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def payfororder(request,pk):
    if request.method == 'POST':
        user = Billing.objects.get(ID=pk)
        total_cash = Billing.objects.get(ID=pk).SumCount
        oder_cost = Orders.objects.get(UserID=pk).Amount

        if total_cash - oder_cost >= 0:
            request.POST._mutable = True
            request.data['SumCount'] = total_cash - oder_cost
            request.data['Message'] = 'Товар успешно оплачен'
            serializer = BillingSerializer(instance=user, data=request.data)


            if serializer.is_valid():
                serializer.save()
                obj = Orders.objects.get(UserID=pk)
                obj.IsPayed = True
                obj.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)



            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Недостаточно средств', status=status.HTTP_400_BAD_REQUEST)

