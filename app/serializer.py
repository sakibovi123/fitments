from rest_framework import serializers
from .models import Category, SubCategory, Brand, MultiImage, Product, Cart, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

