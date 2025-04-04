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






login = [None]*10
senha = [None]*10

login [3]= "DebugUser"
senha [3] = "DebugSenha"

loginUser(login,senha)