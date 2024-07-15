valor = float(input('Digite o valor da peça: '))
sexo = str(input('Insira o sexo (Homem/Mulher): ').lower())

if(sexo == 'homem'):
    casado = str(input('Você é casado? (Sim/Não): ').lower())

valorDescasado = f'{valor:.2f}'
descontoMulher = f'{valor - (valor * 20) / 100:.2f}'
descontoHomem = f'{valor - (valor * 5) / 100:.2f}'

if((sexo == 'homem') and (casado == 'não' or 'nao')):
    print(f'O Valor total da sua compra será de R$100{valorDescasado}')

if((sexo == 'homem') and (casado == 'sim')):
    print(f'Você recebeu um desconto de 5% e o valor da sua compra ficou R${descontoHomem}')
    
if(sexo == 'mulher'):
    print(f'Você recebeu um desconto de 20% e o valor da sua compra ficou R${descontoMulher} | Parabéns pelo dia das mulheres! ')
    
