# valores de cada espaço na lista.

#               0       1           2           3
coisas = ["Exemplo1","Exemplo2","Exemplo3","Exemplo4"]


#ira adicionar um item na lista.
coisas.append("Exemplo5")

#ira adicionar um item a lista no espaço selecionado, assumindo o valor do mesmo.
coisas.insert(2, "Exemplo Extra")

#comando para remover algum item da lista selecionando a sua posição, o mesmo perde o valor, assim o item seguido tomando o valor do mesmo.
coisas.pop(0)

#Comando para voce remover o item da lista, selecionando o mesmo pelo item escrito e não pela sua posição.
coisas.remove("Exemplo2")

#define qual item da lista ira mostrar.
print(coisas[2])

#ira organizar cada item da lista em seu valor de inicio ao final.
for nome in coisas:

    print(nome)