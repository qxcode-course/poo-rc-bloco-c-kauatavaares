class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"

    def gastoPorFolha(self):
        grafites = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return grafites.get(self.dureza, 0)


class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.tip: Grafite | None = None
        self.barrel:list [Grafite] = []

    def insert(self, calibre: float, dureza: str, tamanho: int):
        if calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        grafite = Grafite(calibre, dureza, tamanho)
        self.barrel.append(grafite)


    def remove(self) -> Grafite | None:
        if self.tip is None:
            print("fail: bico vazio")
            return None
        graf_removido = self.tip
        self.tip = None
        return graf_removido

    def pull(self) -> bool:
        if self.tip is not None:
            print("fail: ja existe grafite no bico")
            return False
        elif not self.barrel:
            print("fail: sem grafite")
            return False
        self.tip = self.barrel.pop(0)
        return True

    def writePage(self):
        if self.tip is None:
            print("fail: nao existe grafite no bico")
            return
        elif self.tip.tamanho <= 10:
            print("fail: tamanho insuficiente")
            self.tip = None
            return
        consumo = self.tip.gastoPorFolha()
        if self.tip.tamanho - consumo < 10:
            print("fail: folha incompleta")
            self.tip.tamanho = 10
            return
        else:
            self.tip.tamanho -= consumo

    def __str__(self):
            tip_str = f"[{self.tip}]" if self.tip else "[]"
            barrel_str = "".join(f"[{l}]" for l in self.barrel)
            return f"calibre: {self.calibre}, bico: {tip_str}, tambor: <{barrel_str}>"

def main():
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "insert":
           lapiseira.insert(float(args[1]), args[2], int(args[3]))
        elif args[0] == "pull":
            lapiseira.pull()
        elif args[0] == "remove":
            lapiseira.remove()
        elif args[0] == "write":
            lapiseira.writePage()

main()





