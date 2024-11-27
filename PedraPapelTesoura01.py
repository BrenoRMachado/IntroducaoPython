# 2.1 - Biblioteca para o computador fazer uma escolha aleatória
import random

# 1- Criamos uma função para englobar o jogo

def papelTesoura():
    # 2- Criamos dois jogadores (um usuário e o computador)
    # 3- Fazer o usuário e o computador escolherem suas jogadas
    # jogadas possíveis:

    opcoes = ["pedra","papel","tesoura"]
    # uma variável que tem como elemento uma lista de 3 strings
    # lista é uma estrutura de dados que armazena vários itens em ordem. Podemos acessar os itens por indice    

    # 3.1- O usuário irá digitar o que deseja

    escolhaDoUsuario = input("Escolha pedra, papel ou tesoura: ").lower()
    # função input() pode exibir uma mensagem e capturar um texto digitado pelo usuário
    # .lower() transforma o texto em letras minúsculas para evitar erros de digitação
    



    # 3.2- O computador irá escolher com a função random  
    # 4- Verificamos se os dois empataram (usuario == computador) e imprimimos que houve um empate, caso seja verdadeiro
    # 5- Vamos criar uma função para verificar as opções de vitória (pedra sobre tesoura, tesoura sobre papel ou papel sobre pedra)
    # 5.1- Caso o usuário ganhe, essa função retorna verdadeiro
    # 6- Verificamos o retorno da função do tópico 5 na função principal
    # 6.1- Imprimimos que o usuário ganhou, caso o retorno seja True
    #7- Caso a função não tenha imprimido nada depois desses passos, imprimimos que o usuário perdeu, já que não houve vitória ou empate.
    #8- Por fim, fazemos a função rodar e aproveitamos o jogo!

