from django.shortcuts import render , HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import user
import re


class SignUp(APIView):
    def post(self, request):
        try:
            # Retrieving data into variable
            password = request.data.get('password')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            dob = request.data.get('dob')
            email = request.data.get('email')
            phone = request.data.get('phone')
            user_type = request.data.get('user_type')
            
            # Check the necessary fields 
            if not email or not phone or not password:
                return Response(data="Enter your credentials", status=400)
            
            # Valid check
            if not self.validate_email(email = email):
                return Response(data="Invalid email", status=400)
            if not self.validate_phone(phone = phone):
                return Response(data="Invalid phone", status=400)
            
            # save new user in the database
            user_object = user(email = email, password = password, phone = phone, first_name = first_name, last_name = last_name, dob = dob, user_type= user_type)
            user_object.save()
            
            
            return Response(data="User Registered", status=200)
        except Exception as err:
            print(err)
            return Response(data="Invalid Entry", status=400)
        
    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False
        
    def validate_phone(self, phone):
        if re.match(r'^\d{10}$', phone):
            return True
        return False
    
