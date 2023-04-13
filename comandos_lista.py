valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

print(" está é a lista {} ".format(valores))

contagem = valores.count(7)

print("\n  nessa lista repete o numero 7: {} vezes".format(contagem))

valores.reverse()

print("  a lista está invertida {}".format(valores))

valores.sort()

print("  a lista está ordenada {}".format(valores))

valores2 = [2, 3, 5, 10]

print(" \n A lista é : {}".format(valores2))

tamanho = len(valores2)

print(" \n a lista tem {} elementos".format(tamanho))

soma = sum(valores2)

print(" A soma dos elementos é: {}".format(soma))