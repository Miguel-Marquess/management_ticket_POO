from models.excecoes import IngressoJaComprado

class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self._cpf = cpf
        self.email = email
        self.ingressos = {}

    def comprar_ingresso(self, ingresso): 
        if not ingresso.tipo in self.ingressos.keys():
            self.ingressos[ingresso.tipo] = ingresso
            return "Ingresso Comprado."
        else:
            raise IngressoJaComprado
    def listar_ingressos(self):
        return [i for i in self.ingressos.values()]

    def __repr__(self):
        return f"Cliente: {self.nome} | Email: {self.email} | Ingressos: {[i for i in self.ingressos.keys()]}"
