from rest_framework import serializers
from .models import Contact_Us, Privacy_and_Policy, Terms_of_Use, Shopping_Help


class Privacy_and_PolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = Privacy_and_Policy
        fields = '__all__'


class Contact_UsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'


class Terms_of_UseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Terms_of_Use
        fields = '__all__'


class Shopping_HelpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shopping_Help
        fields = '__all__'
