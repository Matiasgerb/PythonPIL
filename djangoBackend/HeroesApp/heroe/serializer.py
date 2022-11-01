#Rest 
from dataclasses import field
from rest_framework import serializers

# Models
from heroe.models import Hero

#Serializers
class HeroSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Hero
        fields = '__all__'