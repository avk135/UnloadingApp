from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import UserColor
from django.contrib.auth.password_validation import validate_password


class UserColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserColor
        fields = ('color', 'user', )

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class UsersListSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField(read_only=True, source='get_color')
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'color', )
    def get_color(self, obj):
        return UserColor.objects.filter(user=obj).first().color