from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from Related_Links.Serializers import Contact_UsSerializers, Privacy_and_PolicySerializers, Terms_of_UseSerializers, \
    Shopping_HelpSerializers
from Related_Links.models import Contact_Us, Privacy_and_Policy, Terms_of_Use, Shopping_Help


# Create your views here.

class Privacy_and_PolicyViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Privacy_and_PolicySerializers
    queryset = Privacy_and_Policy.objects.all()


class Contact_UsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Contact_UsSerializers
    queryset = Contact_Us.objects.all()


class Terms_of_UseViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Terms_of_UseSerializers
    queryset = Terms_of_Use.objects.all()


class Shopping_HelpViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = Shopping_HelpSerializers
    queryset = Shopping_Help.objects.all()
