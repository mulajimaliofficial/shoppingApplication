from rest_framework import serializers
from shoppingApp.models import *


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ["title", "description", "brand","size","price","image"]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password',
                  'name', "phone_no", "address")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance