from rest_framework import serializers

from client.models import TashqiMijoz, IchkiMijoz


class TashqiMijozSerializer(serializers.ModelSerializer):
     
    def create(self, validated_data):
          return TashqiMijoz.objects.create(**validated_data)

    class Meta:
        model = TashqiMijoz
        fields = '__all__'


class IchkiMijozSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return IchkiMijoz.objects.create(**validated_data)

    class Meta:
        model = IchkiMijoz
        fields = '__all__'