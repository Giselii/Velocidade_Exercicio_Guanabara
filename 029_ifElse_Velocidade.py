#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7.00 por cada KM acima do limite

vel = float(input("Qual a velocidade: "))
if vel > 80:
    print('Você ultrapassou a velocidade permitida')
    multa = vel - 80
    valor = multa * 7
    print('Você ultrapassou {} do limite permitido e pagará {} de multa'.format(multa, valor))
else:
    print('Velocidade permitida! Continue assim!!')


