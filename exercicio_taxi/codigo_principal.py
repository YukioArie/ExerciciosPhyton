def exibir_conta(data_hora_inicio, data_hora_termino, codigo, nome):
    print("-----------------------")
    print("Extrato da Corrida")
    print("-----------------------")
    print("Cód. cliente: {}".format(codigo))
    print("Nome cliente: {}".format(nome))
    print("-----------------------")
    # bandeira 1
    if ((data_hora_inicio.hour>=6) and (data_hora_inicio.hour<=22)):
        valor_corrida = (data_hora_termino-data_hora_inicio)*5.50
        print('Período da corrida: {}'.format(data_hora_termino-data_hora_inicio))
        print('Valor da corrida: {}'.format(valor_corrida))
    # bandeira 2
    if ((data_hora_inicio.hour>22) and (data_hora_inicio.hour<6)):
        valor_corrida = (data_hora_termino-data_hora_inicio)*5.50*1.1
        print('Período da corrida: {}'.format(data_hora_termino-data_hora_inicio))
        print('Valor da corrida: {}'.format(valor_corrida))
        print("-----------------------")
        datetime_object = datetime.datetime.now()
        print(datetime_object)
    
