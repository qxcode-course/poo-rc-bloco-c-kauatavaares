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
        self.__wainting.sort(key=lambda k: k.get_Age())

    def enter(self):
        if not self.__wainting:
            raise ValueError("fail: fila vazia")
        kid = self.__wainting.pop(-1)
        self.__playing.append(kid)
        self.__playing.sort(key=lambda k: k.get_Age())
    def leave(self):
        if self.__playing:
            kid = self.__playing.pop(-1)
            self.__wainting.append(kid)
            self.__wainting.sort(key=lambda k: k.get_Age(), reverse = True)
    def remove(self, name: str):
        for lista in (self.__playing, self.__wainting):
            for kid in lista:
                if kid.getName() == name:
                    lista.remove(kid)
                    return
        print(f"fail: {name} nao esta no pula-pula")
        return

    def __str__(self):
        playing = ", ".join([str(kid) for kid in self.__playing])
        waiting = ", ".join([str(kid) for kid in self.__wainting])
        return f"[{waiting}] => [{playing}]"

def main():
    trampolin = TrampoLine()
    while True:
            line = input()
            print("$" + line)
            args = line.split()
            if args[0] == "end":
                break
            elif args[0] == "arrive":
                name = args[1]
                age = int(args[2])
                kid = Kid(name, age)
                trampolin.addKid(kid)
            elif args[0] == "enter":
                trampolin.enter()
            elif args[0] == "show":
                print(trampolin)
            elif args[0] == "remove":
                trampolin.remove(args[1])
            elif args[0] == "leave":
                trampolin.leave()
            else:
                print("fail: comando invalido")


main()



