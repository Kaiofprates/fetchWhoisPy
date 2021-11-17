from src.integration.RegistroImpl import RequestImpl
from src.integration.CnpjImpl import CnpjImpl


if __name__ == '__main__':
    request = RequestImpl('casadomel.com.br')
    cnpj = request.get_cnpj()['document']
    cnpj_impl = CnpjImpl(cnpj)
    cnpj_impl.get_dados()
