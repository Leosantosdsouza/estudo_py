#importamos o modulo por enteiro.

import exemplo_modulo

valor1 = input(" Digite o primeiro valor: ")
valor2 = input(" Digite o segundo valor: ")

soma = exemplo_modulo.soma(valor1, valor2)

print(" A soma é: {}".format(soma))

#importamos função expecificas:

from exemplo_modulo import subtrair, multiplicação

valor3 = input(" \n Digite outro valor ")
valor4 = input(" Digite mais outro valor ")

subtrair1 = subtrair(valor3, valor4)
multiplicação1 = multiplicação(valor3, valor4)

print(" A subtração dos valores é {}. A multiplicação dos mesmo é {}.".format(subtrair1, multiplicação1))