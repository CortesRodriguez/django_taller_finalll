from rest_framework import serializers
from seminarioApp.models import Inscrito

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'