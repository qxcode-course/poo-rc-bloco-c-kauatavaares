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

    def insert(self, grafite: Grafite) -> bool:
        if grafite.calibre != self.calibre:
            print("fail: nao tem esse calibre")
            return False
        self.barrel.append(grafite)
        return True

    def remove(self) -> Grafite | None:
        if self.tip is None:
            print("fail: bico vazio")
            return None
        graf_removido = self.tip
        self.tip = None
        return graf_removido

    def pull(self) -> bool:
        if self.tip is not None:
            print("fail: ja tem grafite")
            return False
        elif not self.barrel:
            print("fail: sem grafite")
            return False
        self.tip = self.barrel.pop(0)
        return True

    def writePage(self):
        if self.tip is None:
            print("fail: nao tem grafite")
            return
        elif self.tip.tamanho <= 10:
            print("fail: acabou o grafite")
            self.tip = None
            return
        consumo = self.tip.gastoPorFolha()
        if self.tip.tamanho < 10:
            print("fail: tamanho da folha acabou")



