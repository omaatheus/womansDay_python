valor = float(input('Digite o valor da peça: '))
sexo = str(input('Insira o sexo (Homem/Mulher): ').lower())

if(sexo == 'homem'):
    casado = str(input('Você é casado? (Sim/Não): ').lower())

descontoMulher = (valor - ((valor * 20) / 100))
descontoHomem = (valor - ((valor * 5) / 100))

descontoHomemRefactor = f'{descontoHomem:.2f}'
descontoMulherRefactor = f'{descontoMulher:.2f}'

if((sexo == 'homem') and (casado == 'não')):
    print(f'O Valor total da sua compra será de {valor}')

if((sexo == 'homem') and (casado == 'sim')):
    print(f'Você recebeu um desconto de 5% e o valor da sua compra ficou R${descontoHomemRefactor}')
    
if(sexo == 'mulher'):
    print(f'Você recebeu um desconto de 20% e o valor da sua compra ficou R${descontoMulherRefactor} | Parabéns pelo dia das mulheres! ')
    
