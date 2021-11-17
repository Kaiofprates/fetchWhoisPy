from src.integration.requestImpl import RequestImpl

if __name__ == '__main__':
    request = RequestImpl('casadomel.com.br')
    print(request.get_cnpj())
