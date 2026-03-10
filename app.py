from models.palco import Palco
from models.cliente import Cliente
from models.festival import Festival
usuario = Cliente("Jose", "123.456.789-10", "jose@gmail.com")
usuario2 = Cliente("Maria", "098.765.432.10", "maria@gmail.com")
palco= Palco("Copacabana ", {
    "VIP": {
        "preco" : 500,
        "quantidade":  0
    },
    "Backstage" : {
        "preco" : 700,
        "quantidade" : 2
    },
    "Pista" : {
        "preco": 250,
        "quantidade" : 0
    }
})

festival = Festival("Rock in Rio", "2024-12-31", "RJ", palco)
festival.clientes[usuario._cpf] = usuario
print(festival.vender_ingressos("Backstage", usuario))
print(usuario.ingressos)
print(festival.listar_clientes())
print(festival.listar_ingressos())