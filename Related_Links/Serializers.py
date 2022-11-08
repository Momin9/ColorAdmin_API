from rest_framework import serializers
from .models import Contact_Us, Privacy_and_Policy


class Privacy_and_PolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = Privacy_and_Policy
        fields = '__all__'



class Contact_UsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'

