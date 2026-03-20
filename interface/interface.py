from interface.menu import menu, selecionar_tipo
from interface.login import login
from models.festival import Festival
from models.palco import Palco
from models.excecoes import *
from models.cadastro_clientes import Cadastro_Login

palco = Palco("Palco Mundo", {
    "VIP" : {
        "preco" : 500,
        "quantidade" : 3
    },
    "Backstage" : {
        "preco" : 700,
        "quantidade" : 2},
    "Pista" : {
        "preco" : 250,
        "quantidade" : 5}
})
festival = Festival("Rock in Rio", "12-12-2026", "Rio de Janeiro", palco)

def gerenciamento():
    clientes = Cadastro_Login()
    usuario = login(clientes)
    while True:
        try:
            if usuario:
                request = menu(festival.nome)
                if request == "1":
                    tipos = selecionar_tipo(festival.ingressos)
                    ingresso_comprado = festival.vender_ingressos(usuario, tipos)
                    print(f"Ingresso <{ingresso_comprado.tipo}> comprado por {usuario.nome}!")
                elif request == "2":
                    print(clientes.buscar_cliente(usuario.cpf))
                elif request == "3":
                    lista_ingressos = festival.listar_ingressos()
                    for i, q in lista_ingressos.items():
                        print(f"Tipo: {i} | Quantidade: {q["quantidade"]}")
                elif request == "4":
                    nomes_clientes = clientes.listar_clientes()
                    for n in nomes_clientes:
                        print(n)
                elif request == "5":
                    print(f"O Total arrecadado: R${festival.total_arrecadado:_.1f}".replace("_", "."))
                elif request == "6":
                    print("Sistema encerrando! Obrigado!")
                    break
        except (KeyError):
            print("Opcao Invalida.")
        except Exception as e:
            print(e)