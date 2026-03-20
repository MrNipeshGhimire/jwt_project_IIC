from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from ..serializer import UserSerializer,ProductSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from ..models import Product


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"msg":"Product added successfully","data":serializer.data})
        else:
            return Response(serializer.errors)
    
    if request.method == 'GET':
        product  = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
