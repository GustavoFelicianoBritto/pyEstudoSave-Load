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



tempLogin = [None]
tempPassword = [None]


tempLogin[0], tempPassword[0] =registerUser(10,0)


print("resultado")
print(tempLogin[0])
print(tempPassword[0])
