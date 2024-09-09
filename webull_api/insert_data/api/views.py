from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from insert_data.models import Company
from insert_data.api.serializer import CompanySerializer
from rest_framework.response import Response
from rest_framework import status
import requests
class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompanySerializer(instance=instance)

        sym = serializer.data['symbol']
        api_key = '0d44474793aa44c190f3e2af1772cf8d'
        url = f'https://api.twelvedata.com/time_series?symbol={sym}&interval=1day&outputsize=7&apikey={api_key}'

        response = requests.get(url)
        data = response.json()
        # print(data)

        return Response(data={'company': serializer.data, 'market':data})