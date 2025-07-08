# Classe que representa um participante
# do reality show. Cada participante tem
# nome, humor, caracteristicas proprias, 
# aptidao fisica e uma lista de 
# caracteristicas que ele gosta em outra 
# pessoa e outra com as que ele não gosta.

# Para a classe serao utilizados os seguintes atributos:
# > nome -> string
# > humor (como o participante está se sentindo) -> string
# > caracteristicas (definem a personalidade do participante) -> int[]
# > aptidao fisica (resistencia em provas fisicas) -> int (Vai de 0 a 100)
# > gosta (caracteristicas que ele gosta em outra pessoa) -> int[]
# > detesta (caracteristicas que ele NAO gosta em outra pessoa) -> int[]

class Participante():
    def __init__(self, nome : str, 
                 humor : str, 
                 caracteristicas : list[int], 
                 aptidao_fisica : int, 
                 gosta : list[int], 
                 detesta : list[int]):
        self.nome = nome
        self.humor = humor
        self.caracteristicas = caracteristicas
        self.aptidao_fisica = aptidao_fisica
        self.gosta = gosta
        self.detesta = detesta
        return