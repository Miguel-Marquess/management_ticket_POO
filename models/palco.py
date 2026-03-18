class Palco:
    def __init__(self, nome, capacidade: dict):
        self.nome = nome
        self._capacidade = capacidade

    def diminuir_capacidade(self, tipo):
        self._capacidade[tipo]["quantidade"] -=1
    @property
    def capacidade(self):
        return self._capacidade
    def resumo(self):
        return f"Palco: {self.nome} | Max. Capacidade: {sum(i for i in self.capacidade.values())}"
    
    def preco_ingresso(self, tipo):
        return self._capacidade[tipo].get("preco")