from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer,UserCreationSerialier,UserEditionSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class Users(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        users = User.objects.filter(is_removed=False)
        serialized_users = UserSerializer(instance=users,many=True)
        return Response(serialized_users.data,status=status.HTTP_200_OK)
        

class UserDetail(APIView):

    def get(self,request,pk):
        user = User.objects.filter(pk=pk,is_removed=False).first()
        if user is None:
            return Response({'error':'User Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serailized_data = UserSerializer(instance=user)
        return Response(serailized_data.data,status=status.HTTP_200_OK)


class CreateUser(APIView):
    
    def post(self,request):
        serialized_data = UserCreationSerialier(data=request.data)
        if serialized_data.is_valid():
            data = serialized_data.validated_data
            user = User.objects.filter(email=data['email'],is_removed=False).first()
            if user is not None:
                return Response({'error':'This email is Already Taken!','success':False},status=status.HTTP_400_BAD_REQUEST)
            
            user = User(email=data['email'],full_name=data['full_name'])
            user.set_password(data['password'])
            user.save()
            serialized_user = UserSerializer(instance=user)
            return Response(serialized_user.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)


class EditUser(APIView):
    
    def put(self,request,pk):
        user = User.objects.filter(pk=pk,is_removed=False).first()
        if user is None:
            return Response({'error':'User Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serialized_user = UserEditionSerializer(data=request.data,instance=user)
        if serialized_user.is_valid():
            user = serialized_user.save()
            return Response(UserSerializer(instance=user).data,status=status.HTTP_202_ACCEPTED)
        return Response(serialized_user.errors,status=status.HTTP_400_BAD_REQUEST)


class RemoveUser(APIView):

    def delete(self,request,pk):
        user = User.objects.filter(pk=pk,is_removed=False).first()
        if user is None:
            return Response({'error':'User Does Not Exists','success':False},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user.is_removed = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GetUserFromToken(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        serialized_user = UserSerializer(instance=user)
        return Response(serialized_user.data)