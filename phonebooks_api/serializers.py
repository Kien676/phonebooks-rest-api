from rest_framework import serializers
"""A serializer is a feature from the django rest framework that allow you to easily convert data inputs into python objects and vice versa.
so if you want to add post or update functionality to our HelloApiView, then we need to create a serializer to receive the content that we post to the API.

"""
from phonebooks_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIview"""
    """Serializer also validate the content past that api is the correct type , thay you require for that field"""
    name =serializers.CharField(max_length=10)

class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phonebook
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only':True,
                'style': {'input_type' : 'password'}
            }
        }


    def create(self,validated_data):
        user = models.Phonebook.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
