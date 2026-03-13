class IngressoJaComprado(Exception):
    def __str__(self):
        return "Ingresso ja comprado! Nao pode ser comprado novamente."
    
class ClienteNaoExiste(Exception):
    def __str__(self):
        return "Cliente nao esta registrado no sistema."
    
class IngressosEsgotados(Exception):
    def __str__(self):
        return "Ingressos Esgotados. Ate a proxima!"
    
class SenhaIncorreta(Exception):
    def __str__(self):
        return "Senha incorreta! Tente novamente."
    
class ClienteJaExiste(Exception):
    def __str__(self):
        return "Cliente ja esta cadastrado!"