# Exemplo de conta aritimetica

# Operações

"""resultado = 2 + 3 / 2
print( " Resultado: ", resultado)"""

# Calculadora

"""
Script para se fazer a calculadora

algoritmo "Soma"
variaveis
    valor1, valor2, soma, divisao, subtracao, multiplicacao, real
Inicio
    Escreva "Digite o primeiro valor"
    leia valor1
    Escreva "Digite o segundo valor"
    leia valor2
    soma = valor1 + valor2
    Escreva " A soma é", soma
    subtracao " A soma é" , subtracao
    divisao = valor1 / valor2
    Escreva "A soma é", divisao
    multiplicacao = valor1 * valor2
    Escreva " A soma é" , multiplicacao
Fim
"""

print("\nprograma = Calculadora\n")

valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")

aritimetica = input("\nSelecione a função que quer calcular: ")
aritimeticasoma = 1
aritimeticasub = 2
aritimeticamult = 3
aritimeticadiv = 4

soma = float(valor1) + float(valor2)
sub = float(valor1) - float(valor2)
mult = float(valor1) * float(valor2)
div = float(valor1) / float(valor2)

if aritimeticasoma == 1:
    print("A soma é", format(soma))

elif aritimeticasub == 2:
    print("A subtração é", format(sub))

elif aritimeticamult == 3:
    print("A multiplicação é", format(mult))

elif aritimeticadiv == 4:
    print("A divisão é", format(div))