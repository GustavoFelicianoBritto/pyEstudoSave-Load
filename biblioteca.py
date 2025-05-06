import random
import string

#criação de função que retorna senha
def newPassword(size):

    #definindo variavel com todos caracteres (letras e digitos)
    caracteres = string.ascii_letters + string.digits + string.punctuation

    #a senha que vai ser retornada é um valor aleatorio do caracteres repetido X vezes, sendo X o tamanho da senha definido quando chamo a função
    password = "".join(random.choice(caracteres) for i in range(size))
    #print(caracteres)
    return  password

def loginUser(login, senha):
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

def registerUser(debug_maxUser, debug_position_last):
    """
    0 - debug_maxUser = O máximo de usuário permitido no servidor, geralmente uso 10
    1- debug_position_last = posição atual da lista, quantidade de linhas no .txt, para que não sobrescreva

    """

    login = [None]*debug_maxUser
    senha = [None]*debug_maxUser

    login[debug_position_last] = input(f"Bem vindo, digite seu login: ") or f"User{debug_position_last}"
    # salvando login


    senha[debug_position_last] = input(f"Olá, {login[debug_position_last]}. Digite sua nova senha: ") or "0000" #chamar outra função geradora
    # salvando senha

    print(f"Login: {login[debug_position_last]}\nSenha: {senha[debug_position_last]}")

    return login[debug_position_last], senha[debug_position_last]
