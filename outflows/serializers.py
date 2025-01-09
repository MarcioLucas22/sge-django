from outflows.models import Outflow
from rest_framework import serializers

class OutflowSerializer(serializers.ModelSerializer):
      class Meta:
            model = Outflow
            fields = '__all__'