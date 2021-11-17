class Cnpj(object):
    def __init__(self, cnpj):
        self.cnpj = cnpj

    def get_info(self):
        raise NotImplementedError("Subclasses must implement abstract method")
