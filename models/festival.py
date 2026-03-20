from models.cliente import Cliente
from models.excecoes import IngressoJaComprado, ClienteNaoExiste, IngressosEsgotados, SenhaIncorreta, ClienteJaExiste
from models.ingresso import Ingresso, Banca_Ingresso
from models.palco import Palco
import secrets

class Festival:
    def __init__(self, nome: str, data: str, local: str, palco: object):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = palco
        self._ingressos = Banca_Ingresso(palco)
        self._total_arrecadado = 0
    def listar_ingressos(self):
        if sum(i["quantidade"] for i in self._ingressos.capacidade_palco.values()) >= 1:
            return self._ingressos.capacidade_palco
        else:
            raise IngressosEsgotados
    @property
    def ingressos(self):
        return self._ingressos.capacidade_palco.items()
    
    def vender_ingressos(self, cliente, tipo):  #Palco retorna quantos ingresos tem, quantos disponiveis, ele mesmomdiminue a quantidade
        ingresso_vendido = self._ingressos.vender(tipo, cliente)
        self._total_arrecadado +=ingresso_vendido.preco
        return ingresso_vendido
    @property
    def total_arrecadado(self):
        return self._total_arrecadado