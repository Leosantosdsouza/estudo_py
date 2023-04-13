Empressa1 = "adobe - 2013-10-01"
Empressa2 = "apollo - 2018-07-01"
Empressa3 = "canva - 2019-05-01"
Empressa4 = "pdl - 2019-10-01"
Empressa5 = "hurb - 2019-03-01"

senha = 100
ajuda_senha = 4
telefone = 3
nome = 2
email = 1


if Empressa1 == "adobe - 2013-10-01":

    total1 = senha + ajuda_senha + nome + email

if Empressa2 == "apollo - 2018-07-01":

    total2 = email + nome + telefone

if Empressa3 == "canva - 2019-05-01":

    total3 = email + nome + senha

if Empressa4 == "pdl - 2019-10-01":

    total4 = email + nome + telefone

if Empressa5 == "hurb - 2019-03-01":

    total5 = email + nome + senha + telefone


    print(total1, total2, total3, total4, total5)
