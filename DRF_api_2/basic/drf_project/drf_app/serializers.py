from rest_framework import serializers
from .models import data
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=40)
    email=serializers.EmailField()
    contact=serializers.IntegerField()
    age=serializers.IntegerField()
    def create(self, validated_data):
        return data.objects.create(**validated_data)

# class EmpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=data
#         fields='__all__'

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

    # doubt



