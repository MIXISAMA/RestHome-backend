from django.shortcuts import get_object_or_404
from rest_framework import serializers

from old.models import Old
from old.serializers import OldSerializer

from employee.models import Emp, Room, OrderForm

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

class OrderFormSerializer(serializers.ModelSerializer):
    old = OldSerializer(read_only=True)
    username = serializers.CharField(write_only=True)
    class Meta:
        model = OrderForm
        fields = ['date_joined', 'id', 'old', 'company_name', 'status', 'comment', 'mark', 'username']
        read_only_fields = ['date_joined', 'id']
    
    def create(self, validated_data):
        validated_data["old"] = get_object_or_404(Old, username=validated_data.pop("username"))
        return OrderForm.objects.create(**validated_data)
