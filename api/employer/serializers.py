from rest_framework import serializers
from .models import Employer, CONtacts


class EMployerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'url', 'name', 'email', 'identifier', 'phone', 'contacts')


class COntactsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CONtacts
        fields = ('id', 'url', 'name', 'lastname', 'email', 'phone')


