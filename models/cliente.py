from models.excecoes import IngressoJaComprado

class Cliente:
    def __init__(self, nome, cpf, email, senha):
        self.nome = nome
        self._cpf = cpf
        self.email = email
        self._senha = senha
        self.ingressos = {}

    @property
    def senha(self):
        return self._senha
    
    @property 
    def cpf(self):
        return self._cpf

    def comprar_ingresso(self, ingresso): 
        if ingresso.tipo not in self.ingressos.keys():
            self.ingressos[ingresso.tipo] = ingresso
        else:
            raise IngressoJaComprado
    
    def listar_ingressos(self):
        return [i for i in self.ingressos.values()]

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"Cliente: {self.nome} | Email: {self.email} | Ingressos: {[i for i in self.ingressos.keys()]}"
        