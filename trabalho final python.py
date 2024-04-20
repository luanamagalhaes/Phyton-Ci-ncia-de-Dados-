from oo1 import Glicemia
# abrir e capturar as linhas do arquivo dados_glicemia_oo.dat
nome_arquivo = "dados_glicemia_oo.dat"
lista_glicemias = []
with open(nome_arquivo,"r",encoding="utf8") as leitor:
    for linha in leitor:
        # splitar a linha e criar um objeto do tipo Glicemia para cada linha
        vetor_linha = linha.split(";")
        #[Quinta,2012,ac,90,6,2037,246,4]

        # inserir o objeto gerado na lista de glicemias
        #Quinta,2012,ac,90,6,2037,246,4
        obj = Glicemia(vetor_linha[0],vetor_linha[1],vetor_linha[3],vetor_linha[4],vetor_linha[5],vetor_linha[6],vetor_linha[7])
        lista_glicemias.append(obj)

        # operações

lista_glicemias.sort(key = lambda glicemia: glicemia.carb)

print("Quantos dados foram capturados? " + str(len(lista_glicemias)))
for item in lista_glicemias:
    print(item)

#dia normal de glicemia são valores entre 80 e 140
qtd_dias_normais = 0
for item in lista_glicemias:
    if item.valor_glicemia >= 80 and item.valor_glicemia < 140:
        qtd_dias_normais += 1

print("Total de dias em glicemia normal: " + str(qtd_dias_normais))


#ano;glicemia;insulina;carb;kcal
linha = "2024;146;20 0;20"
linha = linha.replace(" ",";")
#manipulação de string: split e replace

vetor_linha = linha.split(";")

print(linha)
print(vetor_linha)

#[2024,146;20;0;20]
#instrucao de repeticao - for
for item in vetor_linha:
    print(item)

# for i in range(len(vetor_linha)):
#     print(vetor_linha[i])    

#regra da glicemia até 80 é abaixo; de 80 a 140 é normal; acima de 140 é acima
if int(vetor_linha[1]) < 80:
    vetor_linha[1] = "Abaixo"
elif int(vetor_linha[1]) < 140:
    vetor_linha[1] = "Normal"
else:
    vetor_linha[1] = "Acima"

#regra de carb até 100 abaixo; de 100 até 200 é normal; acima de 200 é acima
if int(vetor_linha[3]) < 100:
    vetor_linha[3] = "Abaixo"
elif int(vetor_linha[3]) < 200:
    vetor_linha[3] = "Normal"
else:
    vetor_linha[3] = "Acima"

print(vetor_linha)


lista_glicemias = [100,98,78,45,238,390,67,98,100,98,100,98,67,55]


for item in lista_glicemias:    
    if (item < 75):
        print(item, "Abaixo")
    elif (item < 140):
        print(item, "Normal")
    else:
        print(item, "Acima")

print(lista_glicemias)

soma = 0
for item in lista_glicemias:
    soma = soma + int(item)

media = soma / len(lista_glicemias)
print("A média de glicemia: ", media)


#para calcular a mediana é necessário ordenar a estrutura
lista_glicemias.sort()

indice_meio = int(len(lista_glicemias)/2)
print("A mediana de glicemia: ", lista_glicemias[indice_meio])

vezes_hipoglicemia = 0
for item in lista_glicemias:
    if int(item) < 70:
        #vezes_hipoglicemia = vezes_hipoglicemia + 1
        vezes_hipoglicemia += 1

print("Quantidade de vezes de hipoglicemia: ", vezes_hipoglicemia)

#len(lista_glicemias) --- 100%
#vezes_hipoglicemia   --- x
porcentagem_hipoglicemia = vezes_hipoglicemia * 100 / len(lista_glicemias)

print("Porcentagem de hipo: ", porcentagem_hipoglicemia)


valor_moda = ""
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if (item == outro_item):
            ocorrencias += 1
    
    if (ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias


print("A moda: ", valor_moda,"ocorrendo ", qtd_moda,"vezes") 