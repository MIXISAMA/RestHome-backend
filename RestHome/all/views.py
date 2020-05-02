from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TestEndpoint(APIView):
    """
    测试Endpoint
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        return Response("Good Job! It is a GET method.")
    
    def post(self, request):
        return Response("Good Job! It is a POST method.")
    
    def put(self, request):
        return Response("Good Job! It is a PUT method.")
    
    def delete(self, request):
        return Response("Good Job! It is a DELETE method.")