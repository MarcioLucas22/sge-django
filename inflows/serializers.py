from inflows.models import Inflow
from rest_framework import serializers

class InflowSerializer(serializers.ModelSerializer):
      class Meta:
            model = Inflow
            fields = '__all__'