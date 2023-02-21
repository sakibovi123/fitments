from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from.serializer import *


class GET_Category(APIView):
    permission_classes = None
    
    def get(self, request):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class POST_Category(APIView):
    permission_classes = None
    
    def post(self, request):
        serializer_class = CategorySerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "Exception": status.HTTP_400_BAD_REQUEST
            })
            

class PUT_Category(APIView):
    permission_classes = None
    
    def post(self, request, category_id):
        query_object = Category.objects.get(id=category_id)
        data = request.data
        if query_object is not None:
            try:
                query_object.category_title = data["category_title"]
                query_object.category_image = data["category_image"]
                
                query_object.save()
                return Response({
                    "status": status.HTTP_201_CREATED,
                    "message": "Successfully Updated"
                })
            except:
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST
                })
        
        else: return Response({
                    "status": status.HTTP_400_BAD_REQUEST
                })
            

class DELETE_Category(APIView):
    def post(self, reqeust, category_id):
        query_object = Category.objects.get(id=category_id)
        if query_object is not None:
            query_object.delete()
            return Response({
                "status": status.HTTP_202_ACCEPTED,
                "message": "Deleted Successfully"
            })
        else: return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Failed"
        })
        

class GET_Brand(APIView):
    def get(self, reqeust):
        pass
    

class POST_Brand(APIView):
    def post(self, request):
        pass
    

class PUT_Brand(APIView):
    def post(self, reqeust, brand_id):
        pass
    

class DELETE_Brand(APIView):
    def post(self, request, brand_id):
        pass
    

class GET_Products(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "data": serializer_class.data
        })
        

class POST_Products(APIView):
    def post(self, request):
        data = request.data
        product_title = data["product_title"]
        category = data["category"]
        sub_category = data["sub_category"]
        brand = data["brand"]
        main_product_image = data["main_product_image"]
        product_description = data["product_description"]
        
        product = Product(
            product_title = product_title,
            category=category,
            sub_category=sub_category,
            brand=brand,
            main_product_image=main_product_image,
            product_description=product_description
        )
        product.save()
        
        for m in data["multiple_image"]:
            multiImage = MultiImage.objects.get(id=m["id"])
            product.main_product_image.add(multiImage)
            
        product.save()
        
        return Response({
            "status": status.HTTP_201_CREATED,
            "message": "Product added"
        })


class PUT_Products(APIView):
    def post(self, request, product_id):
        query_object = Product.objects.get(id=product_id)
        data = request.data
        query_object.product_title = data["product_title"]
        query_object.category = data["category"]
        query_object.sub_category = data["sub_category"]
        query_object.brand = data["brand"]
        query_object.main_product_image = data["main_product_image"]
        query_object.product_description = data["product_description"]
        
        query_object.save()
        
        for m in data["multiple_image"]:
            multiImage = MultiImage.objects.get(id=m["id"])
            query_object.main_product_image.add(multiImage)
            
        query_object.save()
        
        return Response({
            "status": status.HTTP_201_CREATED,
            "message": "Product Updated"
        })
        

class DELETE_Product(APIView):
    def post(self, request, product_id):
        query_object = Product.objects.get(id=product_id)
        query_object.delete()
        return Response({
            "status": status.HTTP_202_ACCEPTED,
            "message": "Product Deleted"
        })
        

"""
    Cart Functions
"""
class GET_Cart(APIView):
    def get(self, request):
        queryset = Cart.objects.filter(
            user=request.user
        )
        serializer_class = CartSerializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK
        })


class AddToCart(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        cart = Cart(
            user=User.objects.get(id=1)
        )
        cart.save()
        for i in data["products"]:
            cart.products.add(i)

        cart.quantity += data["quantity"]
        cart.save()
        serializer_class = CartSerializer(cart)
        return Response({
            "data": serializer_class.data,
            "status": status.HTTP_201_CREATED,
            "message": "Product added to Cart"
        })