from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from django.http import HttpResponse

from rest_framework.permissions import AllowAny
from rest_framework import generics

from client_management.serializers import WorkSerializer
from client_management.serializers import ClientSerializer
from client_management.serializers import UserRegistrationSerializer
from client_management.models import Work
from client_management.models import Client
from client_management.filters import WorkFilter

def hello(request):
	# return render("Hello")
	return HttpResponse("Hello")


class ClientRegistrationView(generics.CreateAPIView):
	permission_class = (AllowAny,)
	serializer_class = UserRegistrationSerializer


class WorkViewSet(viewsets.ModelViewSet):
  """
  API endpoint for work entity.
  """
  queryset = Work.objects.all().order_by('-created_at')
  serializer_class = WorkSerializer
  filterset_class = WorkFilter
  permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
  """
  API endpoints for client entity.
  """
  queryset = Client.objects.all().order_by('-created_at')
  serializer_class = ClientSerializer
  permission_classes = [permissions.IsAuthenticated]
