from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status


from .models import Users_info
from .serializers import ItemSerializer


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


@api_view(['POST'])
def add_user(request):
    user = ItemSerializer(data=request.data)

    # validating for already existing data
    if Users_info.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_200_OK)
    return Response(user.errors)



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
    user= Users_info.objects.get(pk=pk)
    data = ItemSerializer(instance=user, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    user = get_object_or_404(Users_info, pk=pk)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)