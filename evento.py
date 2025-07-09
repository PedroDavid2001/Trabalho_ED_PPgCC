# evento.py

from participante import Participante


class Evento:
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao

    def eliminar_por_aptidao_fisica(
        self, participantes: list[Participante]
    ) -> list[Participante]:
        """
        Simula um evento de resistência física e elimina o participante com a menor aptidão física.

        Args:
            participantes: Uma lista de objetos Participante atualmente na simulação.

        Returns:
            Uma nova lista de participantes após a eliminação.
        """
        if not participantes:
            print("Não há participantes para o evento de eliminação.")
            return []

        # Encontra o participante com a menor aptidão física
        # Certifique-se de que aptidao_fisica é um atributo acessível e numérico
        participante_eliminado = min(participantes, key=lambda p: p.aptidao_fisica)

        # Remove o participante da lista
        participantes_apos_eliminacao = [
            p for p in participantes if p != participante_eliminado
        ]

        print(f"--- Evento: {self.nome} ---")
        print(f"Descrição: {self.descricao}")
        print(
            f"Participante eliminado por menor aptidão física: {participante_eliminado.nome} (Aptidão: {participante_eliminado.aptidao_fisica})"
        )
        print("---")

        return participantes_apos_eliminacao
