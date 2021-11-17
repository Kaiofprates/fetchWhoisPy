from unittest import TestCase
from src.integration.RegistroImpl import RequestImpl


class TestRequestImpl(TestCase):
    def test_get_cnpj(self):
        content = RequestImpl('casadomel.com.br')
        self.assertEqual(type(content.get_cnpj()), dict)

    def test_get_cnpj_invalid(self):
        content = RequestImpl('casadomel.com.br')
        self.assertNotEqual(content.get_cnpj()['type'], 'cpf')

    def test_get_cnpj_valid(self):
        content = RequestImpl('casadomel.com.br')
        self.assertEqual(content.get_cnpj()['type'], 'cnpj')
