import random, string

def newPassword(size):

    #definindo variavel com todos caracteres (letras e digitos)
    caracteres = string.ascii_letters + string.digits

    #a senha que vai ser retornada é um valor aleatorio do caracteres repetido X vezes, sendo X o tamanho da senha definido quando chamo a função
    password = "".join(random.choice(caracteres) for i in range(size))
    #print(caracteres)
    return  password



#espaço que define um valor debug temporario para quantidade maxima de usuarios
debug_maxUser =10
debug_position_last = 0

login = [None]*debug_maxUser
senha = [None]*debug_maxUser

login [3]= "DebugUser"
senha [3] = "DebugSenha"

#espaço que define um valor debug temporário para a quantidade de contas já inscritas para salvar a nova no próximo slot


status = 0

while status != 1 and status != 2:
    status = int(input("Olá, deseja:\n1- cadastrar 2- logar: "))
    if status == 1:
        login[debug_position_last] = input(f"Bem vindo, digite seu login: ")
        #se a informação não for preenchida, vai entrar como usuario o "user0, user1 etc"
        if not login[debug_position_last]:
            login[debug_position_last] = f"User{debug_position_last}"

        senha[debug_position_last] = input(f"Olá, {login[debug_position_last]}. Digite sua nova senha: ")
        if not senha[debug_position_last]:
            senha[debug_position_last] = newPassword(8)
            print(f"Senha vazia. Nova senha: {senha[debug_position_last]}")
            print(f"Login: {login[debug_position_last]}\nSenha: {senha[debug_position_last]}")
            status = 0
        else:
            status = 0



    elif status == 2:

        loginUser = input(f"Olá, digite seu login: ")
        if loginUser in login:
            for tempIndex, tempUser in enumerate(login):
                if loginUser == tempUser:
                    passwordIndex = tempIndex


            # entrada da senha
            loginPassword = input(f"Olá, {loginUser}. Digite sua senha: ")
            if loginPassword == senha[passwordIndex]:
                print("\nusuário logado")
            else:
                print("\nsenha incorreta!")
        else:
            print("usuário não encontrado")
            status = 0

    else:
        print("Opção inválida\n\n")



