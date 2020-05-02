from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import JsonResponse

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