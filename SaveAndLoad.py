import os
import random

username= os.getlogin()

caminho = fr"C:\Users\{username}\Documents\jessica.txt"

wordListEstados =["acre","alagoas","amapa","amazonas","bahia","ceara","goias","maranhao","paraiba","parana","pernambuco","piaui",
"rondonia","roraima","sergipe","tocantins"]

try:
    #tenta abrir arquivo no caminho, no modo leitura e passa o valor do arquivo pra variavel texto
    with open(caminho, "r") as arquivo:
        texto = arquivo.read()
except(FileNotFoundError):
    #se não existir o arquivo
    #Cria um arquivo no caminho especificado com o nome especificado em caminho, e escreve dentro dele
    with open(caminho, "w") as arquivo:
        for i in range(20):
            randomItem = random.choice(wordListEstados)
            arquivo.write(f"{randomItem}\n")
    #depois de criar o arquivo, abre arquivo no caminho, no modo leitura e passa o valor do arquivo pra variavel texto
    with open(caminho, "r") as arquivo:
        texto = arquivo.read()
finally:
    print(f"{texto}")











