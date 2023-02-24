from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.db import transaction

from client_management.models import Work
from client_management.models import Client


class WorkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Work
    fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
  username = serializers.CharField(max_length=256)
  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password])
  password2 = serializers.CharField(
    write_only=True,
    required=True,
  )
  
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({
          "password": "Password field do not match"
        })
    return attrs

  def create(self, validated_data):
    with transaction.atomic():
      user = User.objects.create(
        username=validated_data["username"],
        email=validated_data["email"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
      )
      user.set_password(validated_data["password"])
      user.save()
      return user

  class Meta:
    model = User
    fields = (
      'username', 'email',
      'first_name', 'last_name', 
      'password', 'password2'
    )


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email')


class ClientSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Client
    fields = ('name', 'user')