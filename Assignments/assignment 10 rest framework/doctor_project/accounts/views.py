from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts.serializers import RegisterSerializer, LoginSerializer

# REGISTER VIEW
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "message": "User created successfully",
                "token": token.key
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LOGIN VIEW
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data['username'],
                password=serializer.data['password']
            )
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                
                return Response({
                    "message": "Login successful",
                    "token": token.key
                })
            
            return Response({"error": "Invalid credentials"}, status=400)
        
        return Response(serializer.errors, status=400)