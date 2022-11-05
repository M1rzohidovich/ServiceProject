from rest_framework.response import Response
from rest_framework.views import APIView
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
        ec = TashqiMijozSerializer(data=request.data)
        ec.is_valid(raise_exception=True)
        ec.save()
        data = ec.data

        return Response(data)
        

class IchkiMijozCreateApi(APIView):

    def post(self, request):
        ic = IchkiMijozSerializer(data=request.data)
        ic.is_valid(raise_exception=True)
        ic.save()
        data = ic.data

        return Response(data)