from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
    
class Corrida:
    def __init__(self, data_hora_inicio):
        self.data_hora_inicio = data_hora_inicio
    
    def is_bandeira_01(self):
        if ((self.data_hora_inicio.hour>22) and (self.data_hora_inicio.hour<6)):
            return False
        else:
            return True

    def inicia_corrida(self):
        return self.data_hora_inicio

    def finaliza_corrida(self):
        delta_tempo_mock = timedelta(hours=0, minutes=15, seconds=0)
        return self.data_hora_inicio + delta_tempo_mock

    def duracao_corrida(self):
        return ((self.finaliza_corrida() - self.data_hora_inicio).seconds)/60

    def calcula_corrida(self):
        if self.is_bandeira_01():
            valor_corrida = 5.50 + (0.50 * self.duracao_corrida())
        else:
            valor_corrida = 5.50 + (0.50 * 1.10 * self.duracao_corrida())
        return valor_corrida



cliente = Cliente("Yukio", 123)
corrida = Corrida(datetime.now())
def imprimir_dados_corrida():
    print('Início da corrida: {}'.format(corrida.inicia_corrida()))
    print('Término da corrida: {}'.format(corrida.finaliza_corrida()))
    print('Duração da corrida: {}'.format(corrida.duracao_corrida()))
    print('Valor da corrida: {}'.format(corrida.calcula_corrida()))
imprimir_dados_corrida()
