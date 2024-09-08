from rest_framework import viewsets
from insert_data.models import Company
from insert_data.api.serializer import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer