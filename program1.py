#Modelagem e simulações computacionais com python
import math
import random as rd

valores = [10,100,1000,10000,50000,10000000]  # cria-se uma lista com numeros 10, 100, 1000.

for n in valores: # laço EXTERNO: na primeira rodada de laço externo, "n" é 10; na segunda rodada, "n" é 100, etc
  ncirc = 0            # inicializamos "ncirc" com 0 antes de comecar o jogo numa certa rodada de laco
  for i in range(0,n): # laco INTERNO: repetimos n vezes, ié, sorteamos n pontos, para cada valor de n no laco externo: primeiro n eh 10; depois n eh 100, etc
    x = rd.random()
    y = rd.random()
    dist = ((x-0.5)**2 + (y-0.5)**2)**0.5
    if dist < 0.5:
      ncirc = ncirc + 1

  # imprimimos resultado e erro apos 10 rodadas, apos 100 rodadas....apos 100000 rodadas
  # note que esta parte fica fora de bloco de laco INTERNO, e dentro de bloco de laco EXTERNO
  print("Número de pontos dentro do círculo:",ncirc)
  print("Número total de pontos:",n)
  p_est = ncirc/n
  pi_est = 4*p_est
  print("Estimativa para p",p_est)
  print("Estimativa para pi",pi_est)
  print("Erro", abs(math.pi - pi_est))
  print() # imprimimos linha vazia

  #A estimativa de pi tende a ficar mais próxima ao passo que aumentamos o valor de "n".