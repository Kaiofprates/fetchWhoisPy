import requests
import json

from src.integration.Registro import Registro
from src.exceptions.NoContentException import NoContentException


class RequestImpl(Registro):

    def __init__(self, registro: str):

        """
              Classe reponsável pelo scrap da página de registros.br
              retorna o documento (cpf,cnpj) de um responsável por um
              domínio .br
        """
        """ todo: adicionar validação para url"""

        baseURl = 'https://rdap.registro.br/domain/'
        self.registro = baseURl+registro

    def get_cnpj(self):
        content = self.get_content_json(self.registro)
        if content['entities'][0]['publicIds']:
            identifier = content['entities'][0]['publicIds'][0]['identifier']
            document = content['entities'][0]['publicIds'][0]['type']
            return {'type': document, 'document': identifier}
        else:
            raise Exception('[NO IDENTIFIER] - falha ao recuperar documento')

    def get_content_json(self, req: str) -> dict:
        try:
            return json.loads(requests.get(req).content.decode('utf-8'))
        except Exception as e:
            raise NoContentException(error=e)
