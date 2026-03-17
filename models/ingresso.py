class Ingresso:
    def __init__(self, tipo, preco, codigo):
        self._tipo = tipo
        self._preco = preco
        self._codigo = codigo
        
    @property
    def tipo(self):
        return self._tipo

    def __str__(self):
        return f"[{self._codigo}] | Tipo: {self._tipo} | Preço: {self._preco}"
    
    def __repr__(self):
        return self.__str__()

