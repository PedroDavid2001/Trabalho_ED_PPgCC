# Classe que representa um participante do reality show.
# Cada participante tem nome, humor, caracteristicas proprias,
# aptidao fisica, raciocinio logico e uma lista de 
# caracteristicas que ele gosta em outra pessoa e outra com 
# as que ele não gosta.

# Para a classe serao utilizados os seguintes atributos:
# > nome -> string
# > humor (como o participante está se sentindo) -> string
# > caracteristicas (definem a personalidade do participante) -> int[]
# > aptidao fisica (resistencia em provas fisicas) -> int (Vai de 0 a 100)
# > raciocinio logico (necessario em provas de conhecimento) -> int (Vai de 0 a 100)
# > gosta (caracteristicas que ele gosta em outra pessoa) -> int[]
# > detesta (caracteristicas que ele NAO gosta em outra pessoa) -> int[]

from typing import Literal
from caracteristica import semelhantes
from caracteristica import Caracteristicas
from humor import Humor
import random as rd


class Participante:
    def __init__(self, nome: str, gosta: list, detesta: list):
        self.nome = nome
        self.caracteristicas: list = selecionar_caracteristicas()
        self.gosta = gosta
        self.detesta = detesta

        self.aptidao_fisica: int = definir_aptidao_fisica(self.caracteristicas)
        self.raciocinio_logico: int = definir_raciocinio_logico(self.caracteristicas)
        self.humor = definir_humor_inicial(self.caracteristicas)
        
        return

    # funciona como um setter de humor
    def humor_atual(self, humor: Humor):
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


def definir_humor_inicial(caracteristicas=[]) -> Humor:

    if Caracteristicas.PREGUICOSO in caracteristicas:
        return Humor.CANSADO

    if any(
        c in caracteristicas
        for c in (Caracteristicas.AMIGAVEL, Caracteristicas.TAGARELA)
    ): return Humor.ALEGRE

    if Caracteristicas.TIMIDO in caracteristicas:
        return Humor.TRISTE

    return Humor.NEUTRO


def definir_aptidao_fisica(caracteristicas=[]) -> int:
    # Gera um valora aleatorio entre 50 e 100
    # para nao iniciar com um valor muito baixo
    apt = rd.randint(50, 100)

    # Reduz a aptidao fisica de participantes preguicosos
    if Caracteristicas.PREGUICOSO in caracteristicas:
        apt -= 30

    return apt

def definir_raciocinio_logico(caracteristicas=[]) -> int:
    # Gera um valora aleatorio entre 50 e 100
    # para nao iniciar com um valor muito baixo
    rac = rd.randint(50, 100)

    # Reduz a aptidao fisica de participantes preguicosos
    if Caracteristicas.INTELIGENTE in caracteristicas:
        rac += 30

    return min(rac, 100)