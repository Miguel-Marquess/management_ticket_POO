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
        self._clientes = {}
        self._ingressos = Banca_Ingresso(palco)

    def buscar_cliente(self, cpf):
        if cpf in self._clientes:    
            return self._clientes.get(cpf)
        else:
            raise ClienteNaoExiste
    def listar_ingressos(self):
        if sum(i["quantidade"] for i in self._ingressos.capacidade_palco.values()) >= 1:
            return self._ingressos.capacidade_palco
        else:
            raise IngressosEsgotados
    @property
    def ingressos(self):
        return self._ingressos.capacidade_palco.items()
    
    def vender_ingressos(self, cliente, tipo):  #Palco retorna quantos ingresos tem, quantos disponiveis, ele mesmomdiminue a quantidade
        return self._ingressos.vender(tipo, cliente)
        
    def listar_clientes(self):
        return [c for c in self._clientes.values()]
    
    def login(self, cpf, senha):
        cliente = self.buscar_cliente(cpf)
        senha_cliente = cliente.senha
        if senha == senha_cliente:
            return "Cliente logado com sucesso!", cliente
        else:
            raise SenhaIncorreta
        
    def cadastrar_cliente(self, nome, cpf, email, senha):
        if cpf not in self._clientes.keys(): 
            usuario = Cliente(nome, cpf, email, senha)
            self._clientes[cpf] = usuario
            return "Cliente cadastrado! Bem vindo.", usuario
        else:
            raise ClienteJaExiste
        
