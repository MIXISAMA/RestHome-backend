from django.shortcuts import get_object_or_404
from rest_framework import serializers

from old.models import Old
from old.serializers import OldSerializer

from employee.models import Emp, Room, OrderForm

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['date_joined', 'username', 'first_name', 'sex', 'telephone', 'address', 'password', 'birthday', 'position']
        read_only_fields = ['date_joined', 'room']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        emp = Emp(**validated_data)
        emp.set_password(password)
        emp.save()
        return emp

class RoomSerializer(serializers.ModelSerializer):
    old = OldSerializer(read_only=True)
    emp = EmpSerializer(read_only=True)
    old_username = serializers.CharField(write_only=True)
    emp_username = serializers.CharField(write_only=True)
    class Meta:
        model = Room
        fields = ['id', 'emp', 'old', 'status', 'old_username', 'emp_username']
    
    def create(self, validated_data):
        if validated_data.__contains__("old_username"):
            validated_data["old"] = get_object_or_404(Old, username=validated_data.pop("old_username"))
        if validated_data.__contains__("emp_username"):
            validated_data["emp"] = get_object_or_404(Emp, username=validated_data.pop("emp_username"))
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.__contains__("old_username"):
            instance.old = get_object_or_404(Old, username=validated_data["old_username"])
        if validated_data.__contains__("emp_username"):
            instance.emp = get_object_or_404(Emp, username=validated_data["emp_username"])
        return instance

class OrderFormSerializer(serializers.ModelSerializer):
    old = OldSerializer(read_only=True)
    username = serializers.CharField(write_only=True)
    class Meta:
        model = OrderForm
        fields = ['date_joined', 'id', 'old', 'company_name', 'status', 'comment', 'mark', 'username', 'company_id']
        read_only_fields = ['date_joined', 'id']
    
    def create(self, validated_data):
        validated_data["old"] = get_object_or_404(Old, username=validated_data.pop("username"))
        return OrderForm.objects.create(**validated_data)

class SimpleOrderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderForm
        fields = ['date_joined', 'id', 'company_name', 'status', 'comment', 'mark', 'company_id']
