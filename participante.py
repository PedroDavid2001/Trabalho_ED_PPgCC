# Classe que representa um participante do reality show.
# Cada participante tem nome, humor, caracteristicas proprias,
# aptidao fisica e uma lista de caracteristicas que ele gosta
# em outra pessoa e outra com as que ele não gosta.

# Para a classe serao utilizados os seguintes atributos:
# > nome -> string
# > humor (como o participante está se sentindo) -> string
# > caracteristicas (definem a personalidade do participante) -> int[]
# > aptidao fisica (resistencia em provas fisicas) -> int (Vai de 0 a 100)
# > gosta (caracteristicas que ele gosta em outra pessoa) -> int[]
# > detesta (caracteristicas que ele NAO gosta em outra pessoa) -> int[]

from caracteristica import semelhantes
from caracteristica import Caracteristicas
import humor
import random as rd


class Participante:
    def __init__(self, nome: str, gosta: list, detesta: list):
        self.nome = nome
        self.caracteristicas: list = selecionar_caracteristicas()
        self.gosta = gosta
        self.detesta = detesta

        self.aptidao_fisica: int = definir_aptidao_fisica(self.caracteristicas)
        self.humor: str = definir_humor_inicial(self.caracteristicas)

        return

    # funciona como um setter de humor
    def humor_atual(self, humor: str):
        self.humor = humor


# Neste arquivo tambem implementei um metodo para gerar participantes
def gerar_participante(nome: str) -> Participante:
    gosta = [c for c in Caracteristicas if rd.randint(0, 1)]
    detesta = [c for c in Caracteristicas if c not in gosta]

    return Participante(nome, gosta, detesta)


# Metodo que retorna uma lista com caracteristicas aleatorias
def selecionar_caracteristicas() -> list:
    # Primeira caracteristica a ser adicionada. A partir
    # dela sao selecionadas as que possuem relacao na
    # matriz de adjacencia "semelhantes". Selecionado
    # um numero aleatorio entre 0 e o ultimo indice da
    # enum "Caracteristicas".
    primeira_caracteristica = rd.choice(list(Caracteristicas))
    caracteristicas = [primeira_caracteristica]

    # Agora na linha da primeira caracteristica sao
    # selecionadas outras caracteristica que possuam
    # relacao com ela.
    relacionadas = [
        c for c, rel in semelhantes[primeira_caracteristica].items() if rel == 1
    ]
    # Como o objetivo de tornar ainda mais
    # aleatoria a geracao de caracteristicas
    # adicionei um "cara ou coroa" para decidir
    # se adiciona ou nao a caracteristica relacionada.
    caracteristicas += [c for c in relacionadas if rd.randint(0, 1)]

    return caracteristicas


def definir_humor_inicial(caracteristicas=[]) -> str:

    if Caracteristicas.PREGUICOSO in caracteristicas:
        return humor.CANSADO

    if any(
        c in caracteristicas
        for c in (Caracteristicas.AMIGAVEL, Caracteristicas.TAGARELA)
    ): return humor.ALEGRE

    if Caracteristicas.TIMIDO in caracteristicas:
        return humor.TRISTE

    return humor.NEUTRO


def definir_aptidao_fisica(caracteristicas=[]) -> int:
    # Gera um valora aleatorio entre 50 e 100
    # para nao iniciar com um valor muito baixo
    apt = rd.randint(50, 100)

    # Reduz a aptidao fisica de participantes preguicosos
    if Caracteristicas.PREGUICOSO in caracteristicas:
        apt -= 30

    return apt


# trecho usado para testar os metodos
# p1 = gerar_participante('Pedro')
# p2 = gerar_participante('Paulo')

# print("Participante 1: ", p1.nome)
# print("aptidao fisica: " , p1.aptidao_fisica)
# print("caracteristicas: " , p1.caracteristicas)
# print("gosta de: " , p1.gosta)
# print("não gosta de: " , p1.detesta)
# print("está se sentindo: " , p1.humor)

# print("Participante 2: " , p2.nome)
# print("aptidao fisica: " , p2.aptidao_fisica)
# print("caracteristicas: " , p2.caracteristicas)
# print("gosta de: " , p2.gosta)
# print("não gosta de: " , p2.detesta)
# print("está se sentindo: " , p2.humor)
