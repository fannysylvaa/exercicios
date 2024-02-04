distancia = float(input('A distância total pecorrida  pelo automóvel em quilômetro: '))
combustível = float (input('A total de combustível gasto em litros é de:'))
consumo = distancia / combustível

print('O consumo médio do automóvel é de {:.2f} Km/L'.format(consumo))