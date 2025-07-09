# Matriz que representa as relacoes entre os participantes 
# (Distancia entre os nodes do grafo Vai de -10 a 10).

from participante import Participante
from participante import gerar_participante

class MatrizRelacoes():
    def __init__(self, lista_participantes : list[Participante]):
        self.relacoes = gerar_matriz(lista_participantes)

def gerar_matriz(participantes : list[Participante]) -> dict:
    matriz = {}
    
    for p1 in participantes:
        matriz[p1.nome] = {}
        for p2 in participantes:
            matriz[p1.nome][p2.nome] = nivel_de_relacao(p1 , p2)
        
    return matriz

def nivel_de_relacao(p1 : Participante, p2 : Participante) -> int:
    relacao : int = 0
    # Compara apenas entre participantes diferentes
    if p1.nome != p2.nome:
        # Aumenta a relacao para cada caracteristica que p1 gosta em p2
        for g in p1.gosta:
            for c in p2.caracteristicas:
                if g == c:
                    relacao += 1
                    
        # Diminui a relacao para cada caracteristica que p1 detesta em p2            
        for g in p1.detesta:
            for c in p2.caracteristicas:
                if g == c:
                    relacao -= 1
    
    return relacao

# trecho de codigo para realizacao de testes
lista_p : list[Participante] = []

lista_p.append(gerar_participante('Pedro'))
lista_p.append(gerar_participante('Paulo'))
lista_p.append(gerar_participante('Carlos'))
lista_p.append(gerar_participante('Maria'))
lista_p.append(gerar_participante('João'))
lista_p.append(gerar_participante('Lucas'))
lista_p.append(gerar_participante('Melissa'))
lista_p.append(gerar_participante('Larissa'))
lista_p.append(gerar_participante('Karen')) 

matriz_r : MatrizRelacoes = MatrizRelacoes(lista_p)
print(matriz_r.relacoes)