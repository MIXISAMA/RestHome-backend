from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

from old.serializers import OldSerializer

from old.models import Old

# Create your views here.

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
