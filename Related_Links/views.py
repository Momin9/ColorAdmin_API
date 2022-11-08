from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from Related_Links.Serializers import Contact_UsSerializers, Privacy_and_PolicySerializers
from Related_Links.models import Contact_Us, Privacy_and_Policy


# Create your views here.

class Privacy_and_PolicyViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Privacy_and_PolicySerializers
    queryset = Privacy_and_Policy.objects.all()


class Contact_UsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Contact_UsSerializers
    queryset = Contact_Us.objects.all()
