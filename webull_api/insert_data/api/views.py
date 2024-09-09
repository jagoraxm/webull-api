from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from insert_data.models import Company
from insert_data.api.serializer import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer