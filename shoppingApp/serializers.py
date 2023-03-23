from rest_framework import serializers
from shoppingApp.models import *


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ["title", "description", "brand","size","price","image"]
