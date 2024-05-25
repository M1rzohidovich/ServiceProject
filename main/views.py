from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import WorkerContact, InternalBlog, ExternalBlog, Announcement
from .serializers import ExternalBlogSerializer, InternalBlogSerializer, WorkerContactSerializer, AnnouncementSerializer


class AnnouncementListApiView(APIView):
    authentication_classes = []

    def get(self, request):
        try:
            ann = Announcement.objects.all()
            announcement_list = AnnouncementSerializer(ann, many=True).data
        except:
            announcement_list = None
        return Response(announcement_list)



class GetExternalBlog(APIView):

    def get(self, request):
        blog = ExternalBlog.objects.all()
        serializer = ExternalBlogSerializer(blog, many=True)

        return Response(serializer.data)


class GetInternalBlog(APIView):

     def get(self, request):
         blog1 = InternalBlog.objects.all()
         serializer = InternalBlogSerializer(blog1, many=True)

         return Response(serializer.data)


class GetWorkerContact(APIView):

    def get(self, request):
        contact = WorkerContact.objects.all()
        serializer = WorkerContactSerializer(contact, many=True)

        return Response(serializer.data)








