from rest_framework import serializers
from forms_test.models import Product

class TestSerializer(serializers.Serializer):
    """Serializa un camop de nombre para nuetra APIView"""
    name = serializers.CharField(max_length=15)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'