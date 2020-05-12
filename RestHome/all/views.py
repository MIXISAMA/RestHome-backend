from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

from all.serializers import CompanySerializer, AnnouncementSerializer

from all.models import Company, Announcement

# Create your views here.

@receiver(post_save, sender=User, dispatch_uid="创建之后要自动生成令牌")
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        """
        账号密码登入
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # response.set_cookie('token', response.data['token'])
        groups = user.groups.all()
        if groups.exists():
            groups = [ group.name for group in groups ]
        else:
            groups = []
        return Response({
            'token': 'Token '+token.key,
            'groups': groups
        })
        

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

class Companies(APIView):
    """
    公司信息
    """
    def get(self, request):
        """
        获取公司信息
        """
        tp = request.GET.get('tp', None)
        if tp is None:
            serializer = CompanySerializer(Company.objects.all(), many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            companies = Company.objects.filter(tp=tp)
            serializer = CompanySerializer(companies, many=True)
            return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        """
        修改公司信息
        """
        data = JSONParser().parse(request)
        company = get_object_or_404(Company, id=id)
        serializer = CompanySerializer(company, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

class Announcements(APIView):
    """
    公告信息
    """
    def get(self, request):
        """
        获取公告信息
        """
        serializer = AnnouncementSerializer(Announcement.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        """
        修改公告信息
        """
        data = JSONParser().parse(request)
        announcement = get_object_or_404(Announcement, id=id)
        serializer = AnnouncementSerializer(announcement, data=data, partial=True)
        if not serializer.is_valid():
            raise ParseError(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
