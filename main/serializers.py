from rest_framework import serializers
from main.models import Announcement, WorkerContact, InternalBlog, ExternalBlog


class AnnouncementSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     return Announcement.objects.create(**validated_data)

    class Meta:
        model = Announcement
        fields = '__all__'


class WorkerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerContact
        fields = '__all__'


class InternalBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalBlog
        fields = '__all__'


class ExternalBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalBlog
        fields = '__all__'
