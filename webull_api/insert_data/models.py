import uuid
from django.db import models
from django.core.exceptions import BadRequest
import requests

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=4)

    def _validate_symbol(self):
        api_key = 'ISVNRcvshig5v_2NpKHn490csi2oGnyb'
        url = f'https://api.polygon.io/v3/reference/tickers?exchange=XNYS&ticker={self.symbol}&apiKey={api_key}'

        response = requests.get(url)
        data = response.json()
        
        print(data['results'])

        if data['results'] == []: 
            raise BadRequest({ 
                'symbol': 'El simbolo no existe en NYSE',
            })
    
    def save(self, *args, **kwargs):
        self._validate_symbol()
        return super().save(*args, **kwargs)
    