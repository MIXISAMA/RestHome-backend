from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from all.models import Company

from employee.serializers import RoomSerializer, OrderFormSerializer, EmpSerializer, SimpleOrderFormSerializer
from employee.models import Room, OrderForm, Emp

# Create your views here.


class Emps(APIView):
    """
    员工信息
    """
    def get(self, request, username=None):
        """
        获取员工信息
        """
        if username is None:
            serializer = EmpSerializer(Emp.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            emp = get_object_or_404(Emp, username=username)
            serializer = EmpSerializer(emp)
            return JsonResponse(serializer.data, safe=False)

    def put(self, request, username):
        """
        修改员工信息
        """
        data = JSONParser().parse(request)
        emp = get_object_or_404(Emp, username=username)
        serializer = EmpSerializer(emp, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        增加员工信息
        """
        data = JSONParser().parse(request)
        serializer = EmpSerializer(data=data)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, username):
        """
        删除员工信息
        """
        get_object_or_404(Emp, username=username).delete()
        return Response()

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
    
    def put(self, request, id):
        """
        修改房间信息
        """
        data = JSONParser().parse(request)
        room = get_object_or_404(Room, id=id)
        serializer = RoomSerializer(room, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        增加房间信息
        """
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, id):
        """
        删除订单
        """
        get_object_or_404(Room, id=id).delete()
        return Response()

class OrderForms(APIView):
    """
    订单信息
    """
    def get(self, request, id=None):
        """
        获取订单信息
        """
        if id is not None:
            order_form = get_object_or_404(OrderForm, id=id)
            serializer = OrderFormSerializer(order_form)
            return JsonResponse(serializer.data, safe=False)
        
        old_username = request.GET.get("old_username")
        if old_username:
            serializer = SimpleOrderFormSerializer(
                OrderForm.objects.filter(old__username = old_username).all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        
        company_id = request.GET.get("company_id")
        if company_id:
            serializer = OrderFormSerializer(
                OrderForm.objects.filter(company_id = company_id).all(), many=True)
            return JsonResponse(serializer.data, safe=False)

        serializer = OrderFormSerializer(OrderForm.objects.all(), many=True)
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
        company = get_object_or_404(Company, id=data["company_id"])
        data["company_name"] = company.name
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
