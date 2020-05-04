from rest_framework import serializers

from all.models import Company, Announcement

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'date_joined', 'name', 'tp', 'telephone', 'address', 'introduce']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'date_joined', 'title', 'author', 'content']
