from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from ..serializer import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


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


def get_token_for_user(user):
    tokens = RefreshToken.for_user(user)
    return {
        'refresh':str(tokens),
        'access': str(tokens.access_token)
    }

        
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    errors = {}
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username:
            errors['username'] = "Username is required"
        
        if not password:
            errors['password'] = "Password is required"
        
        if errors:
            return Response({"error":errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
           user =  authenticate(username=username, password=password)
           if user is not None:
              token =  get_token_for_user(user)
              return Response({"msg":"User logged in successfully","token":token},status=status.HTTP_200_OK)
           else:
               return Response({"error":"Invalid credintals"})
            



    