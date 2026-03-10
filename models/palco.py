class Palco:
    def __init__(self, nome, capacidade: dict):
        self.nome = nome
        self._capacidade = capacidade

    @property
    def capacidade(self):
        return self._capacidade

    def resumo(self):
        return f"Palco: {self.nome} | Max. Capacidade: {sum(i for i in self.capacidade.values())}"