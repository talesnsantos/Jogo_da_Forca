import config
from random import choice
from time import sleep

print("""\033[1;31m
--------------------------
|     JOGO DA FORCA      |
|                        |
|    DESENVOLVIDO POR    |
|    Tales L N Santos    |
--------------------------
\033[m\n""")
print("iniciando...\n")
sleep(3)

class jogoForca:

    def __init__(self, nome):
        self.nome = nome

    def game(self):
        linha = []
        error = 0
        word = choice(config.chaves)
        for letra in word:
            linha.append("_")

        print(config.person[0])
        print(linha)
        while error < 5:
            
            letter = input("Escolha uma Letra \n --> ")

            for cont in range(len(word)):
                if letter in word[cont]:
                    linha[cont] = letter
                    
            print(linha)

            if letter not in linha:
                error += 1
                print(config.person[error])
                print(linha)
                print(f"{error} erros")

            x =''.join(linha)
            #x = str(linha).strip('[]')
            #x.strip(',')
            #x.strip("''")
            print (x)
            if x == word:
                break

        if(error == 5):
            print("VOCE PERDEU, TENTE NOVAMENTE")

        else:
            print(f"PARABENS {self.nome}, VOCE É O VENCEDOR")

        
name = input("Digite seu nome \n--> ").upper()
jogo = jogoForca(name)
jogo.game()
