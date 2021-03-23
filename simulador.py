#simular o uso de um dado
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'voce gostaria de jogar novamente'

        def Iniciar(self):
            resposta = input(self.mensagem)
            if resposta == 'sim':
                self.GerarValorDoDado()


        def GerarValorDoDado(self):
            print(random.randint(self.valorminimo,self.valor_maximo))

        simulador = SimuladorDeDado()
        simulador.Iniciar()
