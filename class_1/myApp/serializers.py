from rest_framework import serializers
from .models import user_register

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_register
        fields = ['id', 'first_name', 'sirName', 'mobileNo', 'email', 'password', 'con_password', 'date_of_birth']
