


'''
dados = {"Nome":"Marcos", "Idade":"30"}
print(dados["Nome"])        #Marcos
print(dados["Idade"])       #30
dados["Sexo"] = "Masc"      #adiciona o índice 'Sexo', com valor 'Masc'
print(dados["Sexo"])        #Masc
del dados["Sexo"]           #apaga o índice
------------------------------------------------------------------------------------------
print(dados)                #imprime o dicionário com os índices e seus respectivos valores
print(dados.items())        #imprime o dicionário com os índices e seus respectivos valores
print(dados.values())       #imprime apenas os valores contidos em cada índice
print(dados.keys())         #imprime apenas os índices
------------------------------------------------------------------------------------------
dados = {"Nome":"Marcos", "Idade":30, "Peso":60}
for key, valores in dados.items():
    print(f"{valores} é {key}")
------------------------------------------------------------------------------------------
brasil = []
estado1 = {"UF":"Paraná", "Sigla":"PR"}
estado2 = {"UF":"Santa Catarina", "Sigla":"SC"}
brasil.append(estado1)                              #adiciona um dicionário numa lista
brasil.append(estado2)
print(brasil[0]["UF"])                      #imprime Paraná
------------------------------------------------------------------------------------------
estado = {}
brasil = []
for i in range(0, 2):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())                #Faz uma cópia do dicionário para a lista

for e in brasil:
    for k, v in e.items():
        print(f"{k}: {v}")

