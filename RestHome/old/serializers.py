from rest_framework import serializers

from old.models import Old

class OldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Old
        fields = ['date_joined', 'username', 'first_name', 'sex', 'room', 'telephone', 'address']
