# o cliente vai informar o quanto está pesando.

peso_total = 0.0

#definimos o range de 1 para 11 vezes que ele pode repetir o peso.

for x in range(1,3):

#calculo tanto do peso atual quanto da media que o cliente vai constar.

    peso_atual = float(input( " Informe seu peso atual "))

    peso_total = peso_atual + peso_total

media = peso_total/11

#Assim que finalizar o range de 11 informações, ira aplicar o calculo e apresentar os valores totais.

print( " O seu peso atual é {}. A media do peso é {}".format(peso_total,media))
