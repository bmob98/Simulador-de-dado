# Criar um simulador de dado com uma interface gráfica

# da biblioteca stdlib que gera números inteiros aleatórios
import random
#para fazer a interface gráfica
import PySimpleGUI as sg

# Nome da classe  e  foi chamado a função construtora
class SimuladorDado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
        self.mensagem = "Você deseja jogar o dado?"

        # O layout vai ser definido como se fosse uma lista
        # Vai ter a caixa maior
        self.layout = [
            # Caixa média
            [sg.Text("Deseja jogar o dado? ")],
            #Caixa pequena
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        
# Vai inicia o jogo, o usuario irá dizer se quer jogar, se sim (ao lado do input foi colocado um upper() para padronizar a resposta) o jogo irá começar e chamará a função GerarValorDoDado, se não irá parar. Para o input foi colocado um tratamento de erro.

    def Iniciar(self):
        #Criar uma janela usando o sg que é o apelido que foi dado ao PySimpleGUI, deu o nome de simulador de dado e  chamamos o layout criado na função construtora
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)
        #ler os valores da tela
        # Irá chamar os eventos e os valores na janela criada a cima que irá ler
        self.eventos, self.valores = self.janela.read()

        
        try:
            #chamando o evento, quando compilado irá apresentar a opção para clicar ou escreve, essas serão as opções aceitas com resposta, caso fuja das opções  irá pedir para escrever novamente

            if self.eventos == "Sim" or self.eventos == "S" or self.eventos == "s" or self.eventos == "sim":
                self.GerarValorDoDado()
            elif self.eventos == "Nao" or self.eventos == "Não" or self.eventos == "NÃO" or self.eventos == "não" or self.eventos == "nao" or self.eventos == "n":
                print("OK! Você não deseja jogar. Até a próxima")
            else:
                print("Por favor digitar Sim ou Não")
        except:
            print("Ocorreu algum erro ao receber sua resposta")

            # O randint vai gerar um valor inteiro aleatório dentro  do intervalo determinado. Dentro do print está passado o intervalo dos valores.

    def GerarValorDoDado(self):
        print(random.randint(self.valor_inicial, self.valor_final))


# aqui houve o instanciamento para o programa rodar
simulador = SimuladorDado()
simulador.Iniciar()
