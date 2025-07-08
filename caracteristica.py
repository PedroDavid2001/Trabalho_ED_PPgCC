# Lista de constantes que representam 
# as possiveis opcoes de caracteristicas 
# para cada participante.

# Optei por criar essas variaveis para 
# acessar mais facilmente os valores.
from enum import Enum

class Caracteristicas(Enum):
    INTELIGENTE = 0
    PROATIVO = 1
    AMIGAVEL = 2
    PREGUICOSO = 3
    TAGARELA = 4
    TIMIDO = 5
    COMPETITIVO = 6
    PACIENTE = 7
    PAVIOCURTO = 8
    ARROGANTE = 9

# Para evitar que as caracteristicas sejam 
# distribuidas aleatoriamente, sera utilizada 
# uma matriz de adjacencia para interligar 
# caracteristicas que possuam alguma semelhanca.

semelhantes = []

for c1 in Caracteristicas:
    linha = []
    for c2 in Caracteristicas:
        linha.append(0)
    semelhantes.append(linha)

# Agora basta preencher os indices que tem relacao com 1.
# E possivel acessa-los com os valores dos proprios itens da enum.
# Para facilitar o preenchimento foi utilizado o ChatGPT para 
# preencher os valores.

semelhantes[Caracteristicas.INTELIGENTE][Caracteristicas.PROATIVO] = 1
semelhantes[Caracteristicas.COMPETITIVO][Caracteristicas.PAVIOCURTO] = 1
semelhantes[Caracteristicas.AMIGAVEL][Caracteristicas.TAGARELA] = 1
semelhantes[Caracteristicas.PACIENTE][Caracteristicas.INTELIGENTE] = 1
semelhantes[Caracteristicas.TIMIDO][Caracteristicas.PREGUICOSO] = 1
semelhantes[Caracteristicas.ARROGANTE][Caracteristicas.PAVIOCURTO] = 1
semelhantes[Caracteristicas.AMIGAVEL][Caracteristicas.PACIENTE] = 1
semelhantes[Caracteristicas.PROATIVO][Caracteristicas.COMPETITIVO] = 1