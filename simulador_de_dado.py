# Criar um simulador de dado

# da biblioteca stdlib que gera números inteiros aleatórios
from logging import exception
import random


class SimuladorDado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
        self.mensagem = "Você deseja jogar o dado?"

# Vai inicia o jogo, o usuario irá dizer se quer jogar, se sim (ao lado do input foi colocado um upper() para padronizar a resposta) o jogo irá começar e chamará a função GerarValorDoDado, se não irá parar. Para o input foi colocado um tratamento de erro.

    def Iniciar(self):
        resposta = input(self.mensagem).upper()
        try:
            if resposta == "SIM" or resposta == "S":
                self.GerarValorDoDado()
            elif resposta == 'NÃO' or resposta == 'N':
                print("OK! Você não deseja jogar. Até a próxima")
            else:
                print("Por favor digitar Sim ou Não")

        except:
            print("Ocorreu algum erro ao receber sua resposta")

            # O randint vai gerar um valor inteiro aleatório dentro  do intervalo determinado. Dentro do print está passado o intervalo dos valores.

    def GerarValorDoDado(self):
        print(random.randint(self.valor_inicial, self.valor_final))


# aqui houve o instanciamento para o programa funcionar
simulador = SimuladorDado()
simulador.Iniciar()
