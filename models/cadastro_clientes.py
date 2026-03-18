from models.excecoes import SenhaIncorreta, ClienteNaoExiste, ClienteJaExiste
from models.cliente import Cliente
class Cadastro_Login:
    def __init__(self):
        self._clientes = {}

    def buscar_cliente(self, cpf):
        if cpf in self._clientes:    
            return self._clientes.get(cpf)
        else:
            raise ClienteNaoExiste
    
    def login(self, cpf, senha):
        cliente = self.buscar_cliente(cpf)
        senha_cliente = cliente.senha
        if senha == senha_cliente:
            return cliente
        else:
            raise SenhaIncorreta
        
    def listar_clientes(self):
        return [c for c in self._clientes.values()]
    
    def cadastrar_cliente(self, nome, cpf, email, senha):
        if cpf not in self._clientes.keys(): 
            usuario = Cliente(nome, cpf, email, senha)
            self._clientes[cpf] = usuario
            return usuario
        else:
            raise ClienteJaExiste