#simular o uso de um dado
import random
import PySimpleGUI

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'voce gostaria de jogar novamente'
        layout =

        def Iniciar(self):
            resposta = input(self.mensagem)
            try:

            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
                elif resposta == 'não' or resposta == 'n':
                    print('Obrigado')

                else:
                    print('Digitar sim ou não')
                except:
                    print('ocorreu um erro na resposta')

        def GerarValorDoDado(self):
            print(random.randint(self.valorminimo,self.valor_maximo))

        simulador = SimuladorDeDado()
        simulador.Iniciar()
