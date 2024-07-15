# No dia da mulher a loja Remmer decidiu fazer uma promoção. Qualquer compra feita por uma mulher terá 20% de desconto e qualquer compra feita por um homem casado terá 5% de desconto. Faça um programa que retorne 
#   - O valor do desconto em porcentagem e em reais  
#   - O valor total a ser pago por uma compra

# Considere: 
# Para calcular o valor do desconto basta multiplicar o valor da compra pelo valor da porcentagem divido por 100. 
# Exemplo: se a compra sem desconto é 50 reais, para dar 5% de desconto basta fazer a conta 50 * 5/100

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
    