from paranuara_challenge.models import Company
from paranuara_challenge.models import Person
from rest_framework import serializers as serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('_id',)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('_id',)

class CommonFriendSeializer(serializers.Serializer):
    person1 = serializers.IntegerField(required=True)
    person2 = serializers.IntegerField(required=True)



