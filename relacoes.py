import math
from participante import Participante


class MatrizRelacoes:
    """
    Representa a matriz de relações entre os participantes.
    As relações variam de -10 a 10.
    """

    def __init__(self, lista_participantes: list[Participante]):
        """
        Inicializa a matriz de relações para uma dada lista de participantes.
        """
        self.relacoes = self.gerar_matriz(lista_participantes)

    @staticmethod
    def gerar_matriz(participantes: list[Participante]) -> dict[str, dict[str, int]]:
        """
        Gera a matriz de relações entre todos os participantes.
        """
        matriz = {}
        for p1 in participantes:
            matriz[p1.nome] = {}
            for p2 in participantes:
                matriz[p1.nome][p2.nome] = MatrizRelacoes.nivel_de_relacao(p1, p2)
        return matriz

    @staticmethod
    def nivel_de_relacao(p1: Participante, p2: Participante) -> int:
        """
        Calcula o nível de relação entre dois participantes.
        Aumenta para características que p1 gosta em p2 e diminui para as que detesta.
        """
        relacao: int = 0
        if p1.nome != p2.nome:

            for gosto in p1.gosta:
                for char in p2.caracteristicas:
                    if gosto == char:
                        relacao += 1

            for desgosto in p1.detesta:
                for char in p2.caracteristicas:
                    if desgosto == char:
                        relacao -= 1
        return relacao
