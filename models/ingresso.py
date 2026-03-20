import secrets
from models.excecoes import IngressosEsgotados
class Ingresso:
    def __init__(self, tipo, preco):
        self._tipo = tipo
        self._preco = preco
        self._codigo = f"<{tipo}>" + secrets.token_hex(4)
        
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f"[{self._codigo}] | Tipo: {self._tipo} | Preço: {self._preco}"
    
    def __repr__(self):
        return self.__str__()

class Banca_Ingresso:
    def __init__(self, palco):
        self._ingressos_disponiveis = palco

    @property
    def capacidade_palco(self):
        return self._ingressos_disponiveis.capacidade
    
    def vender(self, tipo, cliente):
        ingresso = Ingresso(tipo, self._ingressos_disponiveis.preco_ingresso(tipo))
        if self._ingressos_disponiveis.capacidade[tipo].get("quantidade") >= 1:
            cliente.comprar_ingresso(ingresso)
            self._ingressos_disponiveis.diminuir_capacidade(tipo)
            return ingresso 
        raise IngressosEsgotados

    
