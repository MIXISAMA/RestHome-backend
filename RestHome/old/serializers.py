from rest_framework import serializers

from old.models import Old

class OldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Old
        fields = ['username', 'first_name', 'sex', 'room', 'telephone', 'address']
