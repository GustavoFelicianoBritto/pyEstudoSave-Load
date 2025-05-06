from biblioteca import *

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



