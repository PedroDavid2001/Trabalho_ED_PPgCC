# Lista de constantes que representam as possiveis opcoes
# de caracteristicas para cada participante.

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
# uma matriz de adjacencia (grafo) para interligar
# caracteristicas que possuam alguma semelhanca.

semelhantes = {}

for c1 in Caracteristicas:
    semelhantes[c1] = {}
    for c2 in Caracteristicas:
        semelhantes[c1][c2] = 0

# Agora basta preencher os indices que tem relacao com 1.
# E possivel acessa-los com os valores dos proprios itens da enum.

# Lista de pares de caracteristicas semelhantes
pares_semelhantes = [
    (Caracteristicas.INTELIGENTE, Caracteristicas.PROATIVO),
    (Caracteristicas.COMPETITIVO, Caracteristicas.PAVIOCURTO),
    (Caracteristicas.AMIGAVEL, Caracteristicas.TAGARELA),
    (Caracteristicas.PACIENTE, Caracteristicas.INTELIGENTE),
    (Caracteristicas.TIMIDO, Caracteristicas.PREGUICOSO),
    (Caracteristicas.ARROGANTE, Caracteristicas.PAVIOCURTO),
    (Caracteristicas.AMIGAVEL, Caracteristicas.PACIENTE),
    (Caracteristicas.PROATIVO, Caracteristicas.COMPETITIVO),
]

# Preenche a matriz de adjacência de forma bidirecional
for c1, c2 in pares_semelhantes:
    semelhantes[c1][c2] = 1
    semelhantes[c2][c1] = 1
