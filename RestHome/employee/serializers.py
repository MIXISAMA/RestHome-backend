from rest_framework import serializers

from old.serializers import OldSerializer

from employee.models import Emp, Room

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['date_joined', 'username', 'first_name', 'sex', 'telephone', 'address']


class RoomSerializer(serializers.ModelSerializer):
    olds = OldSerializer(many=True)
    emp = EmpSerializer()
    class Meta:
        model = Room
        fields = ['id', 'emp', 'olds', 'status']
