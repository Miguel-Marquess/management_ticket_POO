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

def selecionar_tipo(tipos):
    ingressos = {}
    for p, v in enumerate(tipos, start=1):
        ingressos[p] = v
    print("Selecione um Ingresso".center(40, "-"))
    while True:
        try:
            for p, v in ingressos.items():
                print(f"{p} - {v}")
            return ingressos[int(input("Digite a posicao: \n>>> "))]
        except KeyError:
            print("Digite uma opcao valida.")
        except Exception as e:
            print(e)


# class VIP(Ingresso):
#     def __init__(self):
#         super().__init__(tipo="VIP", preco=500, codigo="<VIP>" + secrets.token_hex(4))

# class Backstage(Ingresso):
#     def __init__(self):
#         super().__init__(tipo="Backstage", preco=700, codigo="<BACK>"+secrets.token_hex(4))

# class Pista(Ingresso):
#     def __init__(self):
#         super().__init__(tipo="Pista", preco=250, codigo="<PST>"+ secrets.token_hex(4))