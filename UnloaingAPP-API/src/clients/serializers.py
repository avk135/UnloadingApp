from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Client, UnLoading
# from rules.serializers import UserSerializer
from django.contrib.auth.models import User
from rules.models import UserColor


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'description', )

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client

class UnLoadingSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = UnLoading
        fields = ('client', 'details', 'price', 'alredy_paid', 'workers', )

    def create(self, validated_data):
        client = validated_data.pop('client')
        workers = validated_data.pop('workers')
        unloading = UnLoading.objects.create(client=client, **validated_data)
        for i in workers:
            unloading.workers.add(i)
        return unloading

class UnLoadingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnLoading
        fields = ('client', 'alredy_paid', )

    def create(self, validated_data):
        client = validated_data.pop('client')
        unloading = UnLoading.objects.create(client=client, **validated_data)
        return unloading

class UnLoadingUserSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField(read_only=True, source='get_color')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'color', )
    def get_color(self, obj):
        return UserColor.objects.filter(user=obj).first().color

class UnLoadingListSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField(read_only=True, source='get_client')
    workers = UnLoadingUserSerializer(read_only=True, many=True)
    class Meta:
        model = UnLoading
        fields = '__all__'

    def get_client(self, obj):
        client = Client.objects.get(id=obj.client.pk)
        return client.name

