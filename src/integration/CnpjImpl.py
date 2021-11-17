from src.integration.Cnpj import Cnpj
import requests
from bs4 import BeautifulSoup


class CnpjImpl(Cnpj):

    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.consulta_url = 'https://cnpjs.rocks/cnpj/'+self.remove_mask()

    def get_dados(self):
        info = self.request_info()
        if info is not None:
            print('No values')
            self.save_to_file('cnpj_'+self.remove_mask()+'.txt')
        else:
            print(info)

    def request_info(self):

        print('Requesting info for CNPJ: ' + self.cnpj)
        print('URL: ' + self.consulta_url)

        response = requests.get(self.consulta_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text('\n')
        else:
            return None

    def remove_mask(self):
        return self.cnpj.replace('.', '').replace('/', '').replace('-', '')

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.request_info())
