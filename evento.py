import random
import math
from participante import Participante
from relacoes import MatrizRelacoes
from caracteristica import Caracteristicas
from humor import Humor


class Evento:
    """
    Representa um evento que ocorre no reality show.
    Pode ser um teste físico, de raciocínio, social ou um paredão.
    """

    def __init__(self, nome: str, descricao: str):
        """
        Inicializa um evento com nome e descrição.
        """
        self.nome = nome
        self.descricao = descricao

    def eliminar_participante(
        self, participantes: list[Participante], tipo_teste: str = "fisico"
    ) -> tuple[list[Participante], Participante | None]:
        """
        Simula um evento de eliminação baseado em aptidão física ou raciocínio lógico.

        Args:
            participantes: Uma lista de objetos (Participante) atualmente na simulação.
            tipo_teste: "fisico" para eliminar por aptidão física, "logico" para raciocínio lógico.

        Returns:
            Uma tupla contendo a nova lista de participantes e o participante eliminado (ou None se ninguém for eliminado).
        """
        if not participantes:
            return [], None

        participante_eliminado: Participante | None = None

        if tipo_teste == "fisico":
            participante_eliminado = min(participantes, key=lambda p: p.aptidao_fisica)
        elif tipo_teste == "logico":
            participante_eliminado = min(
                participantes, key=lambda p: p.raciocinio_logico
            )
        else:
            print(f"Tipo de teste '{tipo_teste}' desconhecido. Ninguém foi eliminado.")
            return participantes, None

        if participante_eliminado:
            # Verifica se há outros participantes com a mesma menor pontuação
            if tipo_teste == "fisico":
                min_score = participante_eliminado.aptidao_fisica
                candidatos_a_eliminar = [
                    p for p in participantes if p.aptidao_fisica == min_score
                ]
            else:  # tipo_teste == "logico"
                min_score = participante_eliminado.raciocinio_logico
                candidatos_a_eliminar = [
                    p for p in participantes if p.raciocinio_logico == min_score
                ]

            if len(candidatos_a_eliminar) > 1:
                # Se houver empate, elimina um aleatoriamente entre os empatados
                participante_eliminado = random.choice(candidatos_a_eliminar)

            participantes_apos_eliminacao = [
                p for p in participantes if p != participante_eliminado
            ]
            return participantes_apos_eliminacao, participante_eliminado

        return participantes, None

    def evento_social(self, participantes: list[Participante]) -> None:
        """
        Simula um evento social que pode mudar o humor dos participantes.
        """
        if not participantes:
            return

        if len(participantes) < 2:
            return

        p1, p2 = random.sample(participantes, 2)

        # Exemplo de interação: se um é tagarela e o outro tímido, o tímido pode ficar irritado ou triste
        if (
            Caracteristicas.TAGARELA in p1.caracteristicas
            and Caracteristicas.TIMIDO in p2.caracteristicas
        ):
            p2.humor_atual(Humor.IRRITADO)

        elif (
            Caracteristicas.AMIGAVEL in p1.caracteristicas
            and p2.humor == Humor.TRISTE
        ):
            p2.humor_atual(Humor.NEUTRO)

        else:
            # Caso geral: humor aleatório para alguns
            for p in random.sample(
                participantes, k=min(len(participantes), 3)
            ):  # Afeta até 3 participantes
                old_humor = p.humor
                possible_humors = [
                    Humor.ALEGRE,
                    Humor.IRRITADO,
                    Humor.CANSADO,
                    Humor.TRISTE,
                    Humor.NEUTRO,
                ]
                new_humor = random.choice(
                    [h for h in possible_humors if h != old_humor]
                )
                p.humor_atual(new_humor)

    def paredao(
        self, participantes: list[Participante]
    ) -> tuple[list[Participante], Participante | None]:
        """
        Simula o evento do Paredão, onde os participantes votam para eliminar alguém.
        O participante com a pior relação é votado.
        """
        if len(participantes) < 2:
            return participantes, None

        votos_em_cada_participante: dict[str, int] = {p.nome: 0 for p in participantes}
        matriz_rel = MatrizRelacoes(participantes)

        # Cada participante vota
        for p1 in participantes:
            menor_relacao = math.inf
            participante_votado_nome: str = ""

            # Busca o participante com a menor relação (pior)
            for p2 in participantes:
                if p1.nome != p2.nome:  # Não pode votar em si mesmo
                    relacao_com_p2 = matriz_rel.relacoes[p1.nome][p2.nome]
                    if relacao_com_p2 < menor_relacao:
                        menor_relacao = relacao_com_p2
                        participante_votado_nome = p2.nome
                    elif relacao_com_p2 == menor_relacao:
                        # Em caso de empate na pior relação, vota aleatoriamente entre os empatados
                        if random.random() > 0.5:
                            participante_votado_nome = p2.nome

            if participante_votado_nome:  # Garante que um participante foi escolhido
                votos_em_cada_participante[participante_votado_nome] += 1

        # Encontra o participante mais votado
        if not votos_em_cada_participante:
            return participantes, None

        mais_votado_nome: str = max(
            votos_em_cada_participante, key=votos_em_cada_participante.get
        )
        maior_voto: int = votos_em_cada_participante[mais_votado_nome]

        # Lida com empates no paredão
        candidatos_a_eliminar_nomes = [
            nome
            for nome, votos in votos_em_cada_participante.items()
            if votos == maior_voto
        ]

        if len(candidatos_a_eliminar_nomes) > 1:
            # Se houver empate, elimina um aleatoriamente entre os mais votados
            mais_votado_nome = random.choice(candidatos_a_eliminar_nomes)

        participante_eliminado: Participante | None = None
        for p in participantes:
            if p.nome == mais_votado_nome:
                participante_eliminado = p
                break

        participantes_apos_eliminacao = [
            p for p in participantes if p != participante_eliminado
        ]

        return participantes_apos_eliminacao, participante_eliminado
