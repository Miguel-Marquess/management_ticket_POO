from models.cliente import Cliente
from models.excecoes import IngressoJaComprado, ClienteNaoExiste, IngressosEsgotados, SenhaIncorreta
from models.ingresso import Ingresso, selecionar_tipo
from models.palco import Palco
import secrets

class Festival:
    def __init__(self, nome: str, data: str, local: str, palco: object):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = palco
        self._clientes = {}
        self.ingressos = palco.capacidade

    def buscar_cliente(self, cpf):
        for cpf_c, cliente in self._clientes.items():
            if cpf_c == cpf:
                return cliente
        else:
            raise ClienteNaoExiste
    
    def listar_ingressos(self):
        if sum(i["quantidade"] for i in self.ingressos.values()) >= 1:
            return self.ingressos
        else:
            raise IngressosEsgotados
    
    def vender_ingressos(self, cliente): 
        tipo = selecionar_tipo(self.ingressos.keys())
        ingresso = Ingresso(tipo, self.ingressos[tipo]["preco"], f"<{tipo}>" + secrets.token_hex(4))
        if self.ingressos[tipo]["quantidade"] >= 1:
            cliente.comprar_ingresso(ingresso)
            self.ingressos[tipo]["quantidade"] -=1
            return f"Ingresso Comprado <{ingresso.tipo}> por {cliente.nome}."
        else:
            raise IngressosEsgotados
        
    def listar_clientes(self):
        return [c for c in self._clientes.values()]
    
    def login(self, cpf, senha):
        cliente = self.buscar_cliente(cpf)
        senha_cliente = cliente.senha
        if senha == senha_cliente:
            return self.vender_ingressos(cliente)
        else:
            raise SenhaIncorreta
    def cadastrar_cliente(self, nome, cpf, email, senha):
        if not self._clientes[cpf]: 
            self.ingressos[cpf] = Cliente(nome, cpf, email, senha)
        return "Cliente cadastrado! Tente fazer Login."