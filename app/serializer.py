from rest_framework import serializers
from .models import Category, SubCategory, Brand, MultiImage, Product, Cart, Order, DeliveryMethod, PaymentMethod


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class MultiImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiImage
        fields = "__all__"
        

class ProductSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source="category.category_title")
    subcategory_title = serializers.CharField(source="subcategory.sub_category_title")
    brand_title = serializers.CharField(source="brand.brand_name")
    class Meta:
        model = Product
        fields = [
            "id", "created_at", "updated_at", "product_title",
            "category_title", "subcategory_title", "brand_title",
            "get_thumbnail", "product_description"
        ]


class CartSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField(source="product.product_title")
    class Meta:
        model = Cart
        fields = [
            "id", "created_at", "updated_at", "cart_id", "products", "quantity"
        ]
        

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = "__all__"