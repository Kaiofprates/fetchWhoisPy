import logging


class NoContentException(Exception):
    def __init__(self, error,  message="Falha ao executar requisição"):
        self.message = message
        super().__init__(self.message)
        logging.error('[REQUEST ERROR] '+str(error))


