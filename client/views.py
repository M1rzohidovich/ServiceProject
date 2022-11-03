from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TashqiMijozSerializer, IchkiMijozSerializer


class TashqiMijozCreateApi(APIView):
    # def get(self, request):
    #     try:
    #         externalclient = TashqiMijoz.objects.all()
    #         externalclient_list = TashqiMijozSerializer(externalclient, many=True).data
    #     except:
    #         externalclient_list = None
    #     return Response(externalclient_list)

    def post(self, request):
            tm = TashqiMijozSerializer(data=request.data)
            tm.is_valid(raise_exception=True)
            tm.save()
            data = tm.data

            return Response(data)
        

class IchkiMijozCreateApi(APIView):

    def post(self, request):
        im = IchkiMijozSerializer(data=request.data)
        im.is_valid(raise_exception=True)
        im.save()
        data = im.data

        return Response(data)