from rest_framework import serializers

from all.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'date_joined', 'name', 'tp', 'telephone', 'address', 'introduce']
