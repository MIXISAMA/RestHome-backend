from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from employee.serializers import RoomSerializer, OrderFormSerializer

from employee.models import Room, OrderForm

# Create your views here.

class Rooms(APIView):
    """
    房间信息
    """
    def get(self, request, id=None):
        """
        获取房间信息
        """
        if id is None:
            serializer = RoomSerializer(Room.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            room = get_object_or_404(Room, id=id)
            serializer = RoomSerializer(room)
            return JsonResponse(serializer.data, safe=False)

class OrderForms(APIView):
    """
    订单信息
    """
    def get(self, request, id=None):
        """
        获取订单信息
        """
        if id is None:
            serializer = OrderFormSerializer(OrderForm.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            order_form = get_object_or_404(OrderForm, id=id)
            serializer = OrderFormSerializer(order_form)
            return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        """
        修改订单信息
        """
        data = JSONParser().parse(request)
        order_form = get_object_or_404(OrderForm, id=id)
        serializer = OrderFormSerializer(order_form, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        增加订单信息
        """
        data = JSONParser().parse(request)
        serializer = OrderFormSerializer(data=data)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, id):
        """
        删除订单
        """
        get_object_or_404(OrderForm, id=id).delete()
        return Response()
