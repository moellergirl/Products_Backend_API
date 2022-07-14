from rest_framework import serializers
from.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        Fields=['title','description','price', 'inventor_quantity']