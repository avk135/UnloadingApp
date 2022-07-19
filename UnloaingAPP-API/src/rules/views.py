from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, UserColorSerializer, UsersListSerializer
from .models import UserColor
from django.contrib.auth.models import User
from rest_framework import status


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

    def post(self, request):
        color = request.data.pop('color')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            user = User.objects.filter(username=serializer.data['username']).first()
            user_color = UserColor.objects.create(user=user, color=color)
            serializer_color = UserColorSerializer(data=user_color)
            if serializer_color.is_valid():
                serializer_color.save()
                return Response({'success': True})
            # return Response(serializer.data)
        return Response(serializer.errors)

class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (IsAuthenticated, )

class UserPermission(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        permission = request.user.is_superuser
        return Response({'is_superuser': permission})

class DeleteUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, id):
        try:
            User.objects.get(pk=id).delete()
            return Response({'seccess': True}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'cant find the model'}, status=status.HTTP_404_NOT_FOUND)