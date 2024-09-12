import uuid
from django.test import TestCase
from unittest.mock import patch
from django.core.exceptions import BadRequest
from insert_data.models import Company

class CompanyModelTest(TestCase):

    def setUp(self):
        self.valid_symbol = "AAPL"  # Un símbolo de ejemplo válido
        self.invalid_symbol = "XXXX"  # Un símbolo de ejemplo inválido

    @patch('requests.get')
    def test_create_company_with_valid_symbol(self, mock_get):
        # Simulamos una respuesta válida de la API
        mock_get.return_value.json.return_value = {
            'results': [{'ticker': self.valid_symbol}]
        }

        company = Company.objects.create(
            name="Apple Inc.",
            description="A technology company",
            symbol=self.valid_symbol
        )

        self.assertEqual(company.symbol, self.valid_symbol)
        self.assertEqual(Company.objects.count(), 1)

    @patch('requests.get')
    def test_create_company_with_invalid_symbol_raises_exception(self, mock_get):
        # Simulamos una respuesta inválida de la API
        mock_get.return_value.json.return_value = {
            'results': []
        }

        with self.assertRaises(BadRequest) as context:
            Company.objects.create(
                name="Invalid Company",
                description="This should fail",
                symbol=self.invalid_symbol
            )

        self.assertIn('symbol', context.exception.args[0])
        self.assertEqual(Company.objects.count(), 0)

    @patch('requests.get')
    def test_validate_symbol_api_called_correctly(self, mock_get):
        # Simulamos una respuesta válida de la API
        mock_get.return_value.json.return_value = {
            'results': [{'ticker': self.valid_symbol}]
        }

        company = Company(
            name="Apple Inc.",
            description="A technology company",
            symbol=self.valid_symbol
        )
        company.save()

        # Verificamos que la URL de la API fue llamada con los parámetros correctos
        api_key = 'ISVNRcvshig5v_2NpKHn490csi2oGnyb'
        expected_url = f'https://api.polygon.io/v3/reference/tickers?exchange=XNYS&ticker={self.valid_symbol}&apiKey={api_key}'
        mock_get.assert_called_once_with(expected_url)

        self.assertEqual(Company.objects.count(), 1)
