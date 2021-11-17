from unittest import TestCase
from src.integration.requestImpl import RequestImpl


class TestRequestImpl(TestCase):
    def test_get_cnpj(self):
        content = RequestImpl('casadomel.com.br')
        self.assertEqual(type(content.get_cnpj()), dict)
