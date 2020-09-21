#Loteria do Tiozão

#Variáveis:

alcance = 60

debug = input('Deseja ver o log?')


cartela = int(input('Quantos números são preenchindos por cartela? '))
simul = int(input('Quantos números serão jogados? '))
garantia = int(input('Qual será a garantia combinatória? '))

#Seleção de dezenas
#Tratamento de erros exige laço fora da liist comprehention

combinação = [int(input(f'Escolha os números que serão jogados, de 1 a {alcance}, sem repetí-los: ')) for i in range(simul)]

#Todas as combinações de simul >escolhe< cartela
from itertools import combinations

comblist = list(combinations(combinação,cartela))
if debug == 's':
    print(comblist)
    print('')
print(f'Foram geradas {len(comblist)} combinações de {cartela} números.')

#Todas as combinações de simul >escolhe< garantia

verif = list(combinations(combinação,garantia))
print(f'Existem {len(verif)} combinações com {garantia} números.')

comblist2 = [[0 for i in range(cartela)]]

if debug == 's':
    for sub in verif:
        print('~~~')
        print(f'Verificando {sub} em verif')
        print('')
        Notprev = True
        for jogo1 in comblist2:
            print(f'verificando {jogo1} em comblist2')
            ('')
            L=0
            for num in sub:
                if num in jogo1:
                    L+=1
            if L==garantia:
                print(L)
                print(f'{sub} encontrado em comblist2')
                Notprev = False
                print(Notprev)
                print('')
        if Notprev:
            Notfound = True
            for jogo2 in comblist:
                if Notfound:
                    print(f'verificando {jogo2} em comblist')
                    print('')
                    M=0
                    for num in sub:
                        if num in jogo2:
                            M+=1
                    if M==garantia:
                        print(f'{sub} encontrado em comblist')
                        comblist2.append(jogo2)
                        print(f'{jogo2} movido para comblist2')
                        Notfound = False
                        print('')
else:
    for sub in verif:
        Notprev = True
        for jogo1 in comblist2:
            if Notprev:
                L=0
                for num in sub:
                    if num in jogo1:
                        L+=1
                if L==garantia:
                    Notprev = False
        if Notprev:
            Notfound = True
            for jogo2 in comblist:
                if Notfound:
                    M=0
                    for num in sub:
                        if num in jogo2:
                            M+=1
                    if M==garantia:
                        comblist2.append(jogo2)
                        Notfound = False

print(f'Bastou apenas {len(comblist2)} combinações de {cartela} números para garantir que todas as combinações de {garantia} números sejam encontradas.')

#Prova dos 9
N=0
notin = 0
itsin = False

for sub in verif:
    for jogo in comblist2:
        for numS in sub:
            if numS in jogo:
                N+=1
        if N==garantia:
            itsin = True
        N=0
    if itsin == False:
        print(f'{sub} não foi encontrado.')
        notin += 1
    itsin = False

print(f'{notin} combinações de {garantia} números foram descartadas')

#Abrindo e tratando (porcamente) os dados passados

import csv

with open('resultados_passados.csv','r') as arquivo:
    passado = list(csv.reader(arquivo))

for i in passado:
    if (type(i) == list):
        for j in i:
            passado[passado.index(i)][i.index(j)] = int(passado[passado.index(i)][i.index(j)])
    passado[passado.index(i)] = tuple(passado[passado.index(i)])

# Cortando resultados passados

for i in comblist2:
    for j in passado:
        if i == j:
            comblist2.remove(i)
            

if input('Deseja ver os resultados no prompt? ') == 's':
    print(f'Sobraram {len(comblist2)} combinações:')
    for i in comblist2:
        print(i)

if input('Deseja arquivar os resultados? ') == 's':
    nome = input('Qual é o nome do arquivo salvo?\n')+'.csv'
    if nome == '.csv':
        nome = 'Jogos Filtrados.csv'
    with open(nome,'w',newline='') as arquivo:
        writer = csv.writer(arquivo,dialect='excel')
        for i in comblist2:
            writer.writerow(i)