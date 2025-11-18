class Kid:
    def __init__(self, name: str, age: int):
        self.__age = None
        self.__name = name
        self.__age = age

    def get_Age(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self, idade_valida: int):
        if idade_valida >= 0:
            self.__age = idade_valida
        else:
            print("fail: ")

    def setName(self, name: int):
        self.__name = name

    def __str__(self):
        return f"{self.__name}:{self.__age}"


class TrampoLine:
    def __init__(self):
        self.__playing: list[Kid] = []
        self.__wainting: list[Kid] = []

    def addKid(self, kid: Kid):
        self.__wainting.append(kid)
        self.__wainting.sort(key=lambda k: k.getAge())

    def enter(self):
        if not self.__wainting:
            raise ValueError("fail: fila vazia")
        else:
            self.__playing.append(self.__wainting.pop(-1))
            self.__playing.sort(key=lambda k: k.getAge())

    def


