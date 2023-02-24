from django.shortcuts import render
from AuthSystem.models import User

from rest_framework import status
from django.db import IntegrityError
from  rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from AuthSystem.serialisers import SignupSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate

# Create your views here.

@csrf_exempt # We need this endpoint to be available without authentication
def signup(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        
        if serializer.is_valid():
            try :
                data = serializer.validated_data # data should be a dictionnary
                user = User.objects.create(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                )

                token = Token.objects.create(user=user)
                return Response({'token':str(token)}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'username taken. choose another username'},
                    status = 400
                )
        else:
            # The case where serializer validation failed
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = serializer.validated_data
        user = authenticate(
            username = data['username'],
            email = data['email'],
            password = data['password'],
        )

        if user is None: # If the authentication failed:
                return Response(
                    {'error': "Unable to login. Check Username and Password!"},
                    status=400
                )
        else: # If the Authentication succeded
            try: # first, we need to verify if a token is already available
                token= Token.objects.get(user=user)
            except: # if none of them is founded, we need to create new one
                token = Token.objects.create(user=UserWarning)
            return Response( # Send the token now...
                {'token':str(token)},
                status=201)