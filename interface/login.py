
def login(banco):
    while True:
        try:
            reposta_login = input("Ja tem conta registrada: [S/n] \n>>> ")
            if reposta_login == "S":
                cpf = input("Digite seu CPF: \n>>> ")
                senha = input("Digite sua senha: \n>>> ")
                return banco.login(cpf, senha)
            elif reposta_login == "n":
                nome_ = input("Digite seu nome: \n>>> ")
                cpf_ = input("Digite seu CPF: \n>>> ")
                email_ = input("Digite seu email: \n>>> ")
                senha_ = input("Digite sua senha: \n>>> ")
                return banco.cadastrar_cliente(nome_, cpf_, email_, senha_) #mensagem, objeto usuario
            else:
                print("Digite uma opcao valida.")
        except Exception as e:
            print(e)