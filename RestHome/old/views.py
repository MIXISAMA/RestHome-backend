from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from old.serializers import OldSerializer

from old.models import Old

# Create your views here.

class Login(APIView):

    permission_classes = []

    def post(self, request):
        """
        注册
        """
        data = JSONParser().parse(request)
        serializer = OldSerializer(data=data)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

class Olds(APIView):
    """
    老人信息
    """
    def get(self, request, username=None):
        """
        获取老人信息
        """
        if username is None:
            serializer = OldSerializer(Old.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            old = get_object_or_404(Old, username=username)
            serializer = OldSerializer(old)
            return JsonResponse(serializer.data, safe=False)

    def put(self, request, username):
        """
        修改老人信息
        """
        data = JSONParser().parse(request)
        old = get_object_or_404(Old, username=username)
        serializer = OldSerializer(old, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        增加老人信息
        """
        data = JSONParser().parse(request)
        serializer = OldSerializer(data=data)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, username):
        """
        删除老人信息
        """
        get_object_or_404(Old, username=username).delete()
        return Response()
