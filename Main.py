import random, string

def newPassword(size):

    #definindo variavel com todos caracteres (letras e digitos)
    caracteres = string.ascii_letters + string.digits

    #a senha que vai ser retornada é um valor aleatorio do caracteres repetido X vezes, sendo X o tamanho da senha definido quando chamo a função
    password = "".join(random.choice(caracteres) for i in range(size))
    #print(caracteres)
    return  password

def registerUser(debug_maxUser, debug_position_last):
    """
    0 - debug_maxUser = O máximo de usuário permitido no servidor, geralmente uso 10
    1- debug_position_last = posição atual da lista, quantidade de linhas no .txt, para que não sobrescreva

    """

    login = [None]*debug_maxUser
    senha = [None]*debug_maxUser

    login[debug_position_last] = input(f"Bem vindo, digite seu login: ") or f"User{debug_position_last}"
    # salvando login


    senha[debug_position_last] = input(f"Olá, {login[debug_position_last]}. Digite sua nova senha: ") or newPassword(8)
    # salvando senha

    print(f"Login: {login[debug_position_last]}\nSenha: {senha[debug_position_last]}")

    return login[debug_position_last], senha[debug_position_last]

def loginUser(login, senha):
    """

    :param login: lista login
    :param senha: lista Senha
    :return:
    """

    loginUser = input(f"Olá, digite seu login: ")
    if loginUser in login:
        for tempIndex, tempUser in enumerate(login):
            if loginUser == tempUser:
                #checando se o login inserido está na lista de login ¹
                #em seguida usando o for pra salvar o index do login e pegar a senha
                #salvando o index da senha para puxar ela como index da lista senha
                passwordIndex = tempIndex

        # entrada da senha
        loginPassword = input(f"Olá, {loginUser}. Digite sua senha: ")
        if loginPassword == senha[passwordIndex]:
            #se a senha inserida for igual a senha da conta no index anteriormente salvo
            print("\nusuário logado")
            return True

        else:
            print("\nsenha incorreta!")
            #mantendo o status 2 para recomeçar a parte de inserir senha
            status = 2

    else:
        print("usuário não encontrado")
        status = 0
        #usuario não encontrado ao digitar o usuario¹


#espaço que define um valor debug temporario para quantidade maxima de usuarios
debug_maxUser =10 #máximo de usuários que será registrado
debug_position_last = 0 #futuramente será a quantidade maxima de linhas + 1 para nova linha

login = [None]*debug_maxUser
senha = [None]*debug_maxUser

login [3]= "DebugUser"
senha [3] = "DebugSenha"

#espaço que define um valor debug temporário para a quantidade de contas já inscritas para salvar a nova no próximo slot


status = 0

while status != 1 and status != 2:
    status = int(input("Olá, deseja:\n1- cadastrar 2- logar: "))
    if status == 1:
        #login e senha na posição atual = retorno da função que registra user e senha
        login[debug_position_last], senha[debug_position_last] = registerUser(debug_maxUser,debug_position_last)
        status =0

    elif status == 2:
        while status ==2:
            #login chamando a função de login com parametro das listas Main login e senha, salvando o return para dar break
            statusLogin = loginUser(login,senha)
            if statusLogin:
                break

    else:
        print("Opção inválida\n\n")



