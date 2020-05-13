from django.shortcuts import get_object_or_404
from rest_framework import serializers

from old.models import Old
from employee.models import Room

class OldSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(write_only=True, allow_null=True)
    class Meta:
        model = Old
        fields = ['date_joined', 'username', 'first_name', 'sex', 'room', 'telephone', 'address', 'password', 'room_id', 'birthday']
        read_only_fields = ['date_joined', 'room']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        room_id = validated_data.pop("room_id")
        if room_id is not None:
            validated_data["room"] = get_object_or_404(Room, id=room_id)
        password = validated_data.pop('password')
        old = Old(**validated_data)
        old.set_password(password)
        old.save()
        return old
