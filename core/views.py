from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from .serializers import *

# Signup API
class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')
        address = request.data.get('address')

        # Validate required fields
        if not username or not email or not password:
            return Response({'error': 'Username, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user already exists
        if CustomUser.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response({'error': 'User with this username or email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': list(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
            address=address
        )

        # Return success response
        return Response({'success': 'User created successfully.'}, status=status.HTTP_201_CREATED)

# Signin API

class SigninAPIView(APIView):
    def post(self, request):
        get_user = request.data.get("username")
        password = request.data.get("password")
        
        cond = Q(Q(username=get_user) | Q(email=get_user))
        user = CustomUser.objects.filter(cond).first()

        if not user:
            return Response({'error': 'Invalid username or email.'}, status=status.HTTP_404_NOT_FOUND)

        # Authenticate user
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'success': True,
                'token': token.key,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

# Signout API
class SignoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()

        return Response({'success': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    

# Product Browsing
class ProductListAPIView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


# Order Creation
class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)