from typing import Literal
from caracteristica import semelhantes, Caracteristicas
from humor import Humor
import random as rd


class Participante:
    """
    Representa um participante do reality show.

    Args:
        nome (str): Nome do participante.
        caracteristicas (list[Caracteristicas]): Lista de características próprias do participante.
        gosta (list[Caracteristicas]): Lista de características que o participante gosta em outros.
        detesta (list[Caracteristicas]): Lista de características que o participante detesta em outros.
        aptidao_fisica (int): Aptidão física do participante (0-100).
        raciocinio_logico (int): Raciocínio lógico do participante (0-100).
        humor (Humor): Humor atual do participante.
    """

    def __init__(
        self, nome: str, gosta: list[Caracteristicas], detesta: list[Caracteristicas]
    ):
        self.nome = nome
        self.caracteristicas: list[Caracteristicas] = self.selecionar_caracteristicas()
        self.gosta = gosta
        self.detesta = detesta

        self.aptidao_fisica: int = self.set_aptidao_fisica(self.caracteristicas)
        self.raciocinio_logico: int = self.set_raciocinio_logico(self.caracteristicas)
        self.humor = self.set_humor_inicial(self.caracteristicas)

    def humor_atual(self, humor: Humor):
        """Atualiza o humor atual do participante."""
        self.humor = humor

    @classmethod
    def gerar_participante(cls, nome: str) -> "Participante":
        """
        Gera uma nova instância de Participante com características, gostos e desgostos aleatórios.
        """
        gosta = [c for c in Caracteristicas if rd.randint(0, 1)]
        detesta = [c for c in Caracteristicas if c not in gosta]
        return cls(nome, gosta, detesta)

    @staticmethod
    def selecionar_caracteristicas() -> list[Caracteristicas]:
        """
        Retorna uma lista de características aleatórias para um participante,
        baseando-se nas relações de semelhança.
        """
        primeira_caracteristica = rd.choice(list(Caracteristicas))
        caracteristicas = [primeira_caracteristica]

        relacionadas = [
            c for c, rel in semelhantes[primeira_caracteristica].items() if rel == 1
        ]

        caracteristicas += [c for c in relacionadas if rd.randint(0, 1)]
        return caracteristicas

    @staticmethod
    def set_humor_inicial(caracteristicas: list[Caracteristicas]) -> Humor:
        """Define o humor inicial do participante com base em suas características."""
        if Caracteristicas.PREGUICOSO in caracteristicas:
            return Humor.CANSADO

        if any(
            c in caracteristicas
            for c in (Caracteristicas.AMIGAVEL, Caracteristicas.TAGARELA)
        ):
            return Humor.ALEGRE

        if Caracteristicas.TIMIDO in caracteristicas:
            return Humor.TRISTE

        return Humor.NEUTRO

    @staticmethod
    def set_aptidao_fisica(caracteristicas: list[Caracteristicas]) -> int:
        """Define a aptidão física do participante (0-100) com base em suas características."""
        apt = rd.randint(50, 100)
        if Caracteristicas.PREGUICOSO in caracteristicas:
            apt -= 30
        return max(0, apt)  # Garante que a aptidão não seja negativa

    @staticmethod
    def set_raciocinio_logico(caracteristicas: list[Caracteristicas]) -> int:
        """Define o raciocínio lógico do participante (0-100) com base em suas características."""
        rac = rd.randint(50, 100)
        if Caracteristicas.INTELIGENTE in caracteristicas:
            rac += 30
        return min(rac, 100)  # Garante que o raciocínio não ultrapasse 100
