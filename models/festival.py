from models.cliente import Cliente
from models.excecoes import IngressoJaComprado, ClienteNaoExiste, IngressosEsgotados
from models.ingresso import Ingresso
from models.palco import Palco
import secrets

class Festival:
    def __init__(self, nome: str, data: str, local: str, palco: object):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = palco
        self.clientes = {}
        self.ingressos = palco.capacidade
    
    def listar_ingressos(self):
        if sum(i["quantidade"] for i in self.ingressos.values()) >= 1:
            return self.ingressos
        else:
            raise IngressosEsgotados
    
    def vender_ingressos(self, tipo, cliente):
        for c in self.clientes.values():
            if c == cliente: 
                ingresso = Ingresso(tipo, self.ingressos[tipo]["preco"], f"<{tipo}>" + secrets.token_hex(4))
                if self.ingressos[tipo]["quantidade"] >= 1:
                    self.ingressos[tipo]["quantidade"] -=1
                else:
                    raise IngressosEsgotados
                return c.comprar_ingresso(ingresso)
        else:
            raise ClienteNaoExiste
        
    def listar_clientes(self):
        return [c for c in self.clientes.values()]