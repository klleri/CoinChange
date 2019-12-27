# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:11:47 2019

@author: Lucas
"""
def altera(moedasListaValores,altera,minMoedas,moedasUsadas):
   for moed in range(altera+1):
      contadorMoedas = moed
      novaMoeda = 1
      for j in [c for c in moedasListaValores if c <= moed]:
            if minMoedas[moed-j] + 1 < contadorMoedas:
               contadorMoedas = minMoedas[moed-j]+1
               novaMoeda = j
      minMoedas[moed] = contadorMoedas
      moedasUsadas[moed] = novaMoeda
   return minMoedas[altera]

def main():
    with open('troco.txt', 'r') as f:
        arquivo = [linha.strip() for linha in f if linha.strip()] 
    
    #Definindo variaveis
    amnt = int(arquivo[0])
    del(arquivo[0])
    clist = []
    moedasAUX = []
    
    #Pre Processamento de dados do arquivo
    moedasAUX.append(arquivo[0].split())
    for a in moedasAUX:
        for b in a:
            clist.append(int(b))
    moedasUsadas = [0]*(amnt+1)
    contadorMoedas = [0]*(amnt+1)
    
    arquivo = open('resposta.txt', 'w')
    arquivo.write("Total value: {} \n".format(amnt))
    miau = altera(clist,amnt,contadorMoedas,moedasUsadas)
    print(miau)
    arquivo.write("how many coins were used: {}".format(miau))
    arquivo.close()
main()