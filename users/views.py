import json
import re
import bcrypt
import jwt
from datetime import datetime, timedelta

from django.views import View
from django.http import JsonResponse

from users.models import User
from my_settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        data               = json.loads(request.body)
        account_name_regex = re.compile(r'^[a-z]+[a-z0-9]{6,16}$')
        email_regex        = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        password_regex     = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])(?!.*?\d{4})(?=.*[a-z])(?=.*[!@#$%^*+=-]).{10,16}$')

        try:
            account_name  = data['account_name']
            password      = data['password']
            name          = data['name']
            email         = data['email']
            phone_number  = data['phone_number']
            address       = data['address']
            gender        = data['gender']
            date_of_birth = data['date_of_birth']

            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "EXIST USER"}, status = 400)
            
            if not account_name_regex.match(account_name):
                return JsonResponse({"message" : "INVALID_ACCOUNT"}, status = 400)

            if not email_regex.match(email):
                return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)

            if not password_regex.match(password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)
            
            User.objects.create(
                account_name  = account_name,
                password      = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'), 
                name          = name, 
                email         = email, 
                phone_number  = phone_number, 
                address       = address, 
                gender        = gender, 
                date_of_birth = date_of_birth
            )
            return JsonResponse({"message" : "SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            account_name  = data['account_name']
            password      = data['password']

            if User.objects.filter(account_name = account_name).exists():
                user_account_name = User.objects.get(account_name = account_name)
                if bcrypt.checkpw(password.encode('utf-8'), user_account_name.password.encode('utf-8')):
                    token = jwt.encode({'exp' : (datetime.utcnow() + timedelta(seconds=360)), 'id' : user_account_name.id}, SECRET_KEY, algorithm='HS256')
                  
                    return JsonResponse({"message" : "LogIn Success", "Token" : token}, status = 200)
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 401)
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        except Exception as e:
            return JsonResponse({"message" : e}, status = 500)
