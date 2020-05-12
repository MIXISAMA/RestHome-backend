from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView

from employee.serializers import RoomSerializer

from employee.models import Room

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
