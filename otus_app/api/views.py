from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken


from .models import Users_info
from accounts.models import CustomUser
from .serializers import ItemSerializer
from accounts.serializers import UserSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_users': '/',
        'Search by UsersName': '/?category=category_name',
        'Search by UserFirstName': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)




@api_view(['GET'])
def view_users(request):
    # checking for the parameters from the URL
    if request.query_params:
        users = Users_info.objects.filter(**request.query_params.dict())
    else:
        users = Users_info.objects.all()

    # if there is something in items else raise error
    if users:
        serializer = ItemSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_user(request, pk):
    user = Users_info.objects.get(pk=pk)
    data = ItemSerializer(instance=user, data=request.data)

    user_id_by_token = Token.objects.get(key=request.auth.key).user_id
    user_raw_by_id = CustomUser.objects.get(id=user_id_by_token)
    user_info = Users_info.objects.get(ID=pk).UserName

    if data.is_valid():
        if str(user_info) == str(user_raw_by_id):
            data.save()
            return Response(data.data, status = status.HTTP_200_OK )
        else:
            return Response(f'Связки логина и токена не существует')
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_items(request, pk):
    user = get_object_or_404(Users_info, pk=pk)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def getbyid(request):
    if request.method == 'GET':
        user_id = Token.objects.get(key=request.auth.key).user_id

        user_info = Users_info.objects.filter(ID=user_id)
        serializer = ItemSerializer(instance=user_info,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)