from rest_framework import serializers
from shoppingApp.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "brand","size","price","image"]
    