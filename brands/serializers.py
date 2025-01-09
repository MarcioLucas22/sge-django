from brands.models import Brand
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
      class Meta:
            model = Brand
            fields = '__all__'