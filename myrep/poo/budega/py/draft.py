class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def __str__(self):
        return self.__nome

class Mercantil:
    def __init__(self, qtd_caixas: int):
        self.