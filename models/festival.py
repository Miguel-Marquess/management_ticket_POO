from models.cliente import Cliente
from models.excecoes import IngressoJaComprado, ClienteNaoExiste, IngressosEsgotados, SenhaIncorreta
from models.ingresso import Ingresso, Selecionar_tipo
from models.palco import Palco
import secrets
cliente = Cliente("Jose", "123.456.789-10", "jpse@gmail.com", "1234")

class Festival:
    def __init__(self, nome: str, data: str, local: str, palco: object):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = palco
        self._clientes = {
            "123.456.789-10" : cliente
        }
        self.ingressos = palco.capacidade

    def buscar_cliente(self, cpf):
        for cpf_c, cliente in self._clientes:
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
        tipo = Selecionar_tipo(self.ingressos.keys())
        ingresso = Ingresso(tipo, self.ingressos[tipo]["preco"], f"<{tipo}>" + secrets.token_hex(4))
        if self.ingressos[tipo]["quantidade"] >= 1:
            self.ingressos[tipo]["quantidade"] -=1
        else:
            raise IngressosEsgotados
        return cliente.comprar_ingresso(ingresso)

        
    def listar_clientes(self):
        return [c for c in self._clientes.values()]
    
    def login(self, cpf, senha):
        cliente = self.buscar_cliente(cpf)
        senha_cliente = cliente.senha
        if senha == senha_cliente:
            return self.vender_ingressos(cliente)
        else:
            raise SenhaIncorreta
    def cadastrar_cliente(self):
