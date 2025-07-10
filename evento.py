from participante import Participante


class Evento:
    # Construtor recebe um boolean como flag para definir 
    # qual o tipo de parametro deve ser usado para 
    # eliminar um participante. 
    # > TRUE = aptidao fisica
    # > FALSE = raciocinio logico
    def __init__(self, nome: str, descricao: str, teste_fisico : bool = True):
        self.nome = nome
        self.descricao = descricao
        self.teste_fisico = teste_fisico
    
    def eliminar_participante(self, participantes: list[Participante]):
        
        if not participantes:
            print("Não há participantes para o evento de eliminação.")
            return []
        
        if self.teste_fisico:
            # Encontra o participante com a menor aptidão física
            participante_eliminado = min(participantes, key=lambda p: p.aptidao_fisica)
        else:
            # Encontra o participante com o menor raciocinio logico
            participante_eliminado = min(participantes, key=lambda p: p.raciocinio_logico)
            
        # Remove o participante da lista
        participantes_apos_eliminacao = [
            p for p in participantes if p != participante_eliminado
        ]
        
        print(f"--- Evento: {self.nome} ---")
        print(f"Descrição: {self.descricao}")
        
        if self.teste_fisico:
            print(
                f"Participante eliminado por menor aptidão física: {participante_eliminado.nome} (Aptidão: {participante_eliminado.aptidao_fisica})"
            )
        else:
            print(
                f"Participante eliminado por menor raciocínio lógico: {participante_eliminado.nome} (Raciocínio: {participante_eliminado.raciocinio_logico})"
            )
        print("---")

        return participantes_apos_eliminacao, participante_eliminado