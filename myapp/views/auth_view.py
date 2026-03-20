from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from ..serializer import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):

    if request.method  == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # return print(username,email,password)
        if User.objects.filter(username=username).exists():
            return Response({"error":"Username already exists !!"},status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error':"Email already exists !! "})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password )
        user.save()
        if user is not None:
            return Response(
                {"msg":"User registered successfully"},
                status=status.HTTP_201_CREATED )
        else:
            return Response({"error":"Failed to register user "})

        
    


    