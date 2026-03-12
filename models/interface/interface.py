from models.interface.menu import menu
from models.interface.login import login
from models.festival import Festival
from models.palco import Palco

palco = Palco("Palco Mundo", {
    "VIP" : {
        "preco" : 500,
        "quantidade" : 3
    },
    "Backstage" : {
        "preco" : 700,
        "quantidade" : 2},
    "Pista" : {
        "preco" : 500,
        "quantidade" : 5}
})
festival = Festival("Rock in Rio", "12-12-2026", "Rio de Janeiro", palco)
def gerenciamento():
    while True:
        request = menu(festival.nome)
        if request == "1":
            print(login(festival))
        elif request == "3":
            lista_ingressos = festival.listar_ingressos()
            for i, q in lista_ingressos.items():
                print(f"Tipo: {i} | Quantidade: {q["quantidade"]}")
