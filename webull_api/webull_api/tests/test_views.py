from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch
from insert_data.models import Company
from django.contrib.auth.models import User

class CompanyViewSetTest(APITestCase):

    def setUp(self):
        # Crear un usuario para autenticación
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Crear una instancia de la compañía
        self.company = Company.objects.create(
            name="Apple Inc.",
            description="A technology company",
            symbol="AA"
        )

    def test_access_denied_if_not_authenticated(self):
        # Crear un cliente no autenticado
        client = APIClient()
        url = reverse('company-detail', args=[self.company.id])

        # Hacer una solicitud sin autenticación
        response = client.get(url)
        
        # Verificar que el acceso sea denegado
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch('requests.get')
    def test_retrieve_company_data_with_market_info(self, mock_get):
        # Simular una respuesta válida de la API externa
        mock_get.return_value.json.return_value = {
            "meta": {"symbol": "AA"},
            "values": [
                {"datetime": "2024-09-01", "close": "150.00"},
                {"datetime": "2024-08-31", "close": "149.00"}
            ]
        }

        url = reverse('company-detail', args=[self.company.id])
        
        # Hacer una solicitud GET autenticada
        response = self.client.get(url)
        
        # Verificar que la solicitud sea exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que los datos de la empresa están presentes en la respuesta
        self.assertEqual(response.data['company']['symbol'], "AA")

        # Verificar que los datos del mercado están presentes en la respuesta
        self.assertIn("meta", response.data['market'])
        self.assertIn("values", response.data['market'])

    @patch('requests.get')
    def test_retrieve_company_with_invalid_market_data(self, mock_get):
        # Simular una respuesta inválida de la API externa (por ejemplo, símbolo no encontrado)
        mock_get.return_value.json.return_value = {
            "code": 400,
            "message": "Invalid symbol"
        }

        url = reverse('company-detail', args=[self.company.id])

        # Hacer una solicitud GET autenticada
        response = self.client.get(url)

        # Verificar que la solicitud sea exitosa, pero con datos de mercado inválidos
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("company", response.data)
        self.assertIn("market", response.data)
        self.assertEqual(response.data['market']['code'], 400)
        self.assertEqual(response.data['market']['message'], "Invalid symbol")
