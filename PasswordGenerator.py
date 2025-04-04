import random
import string

#criação de função que retorna senha
def newPassword(size):

    #definindo variavel com todos caracteres (letras e digitos)
    caracteres = string.ascii_letters + string.digits

    #a senha que vai ser retornada é um valor aleatorio do caracteres repetido X vezes, sendo X o tamanho da senha definido quando chamo a função
    password = "".join(random.choice(caracteres) for i in range(size))
    #print(caracteres)
    return  password





senha = newPassword(8)


print(senha)