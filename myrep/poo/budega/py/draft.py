class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def __str__(self):
        return self.__nome

class Mercantil:
    def __init__(self, qtd_caixas: int):
        self.__caixas:list[Cliente|None] = [None] * qtd_caixas
        self.__fila:list[Cliente|None] = []

    def addPessoa(self, cliente:Cliente):
        self.__fila.append(cliente)

    def callCliente(self, caixa_index: int):
        if not self.__fila:
            print("fail: sem clientes")
            return
        elif  caixa_index < 0 or caixa_index >= len(self.__caixas):
                print("fail: caixa inexistente")
                return
        elif self.__caixas[caixa_index] is not None:
            print("fail: caixa ocupado")
            return
        self.__caixas[caixa_index] = self.__fila.pop(0)
    def finish(self, caixa_index: int):
        if caixa_index < 0 or caixa_index >= len(self.__caixas):
            print("fail: caixa inexistente")
            return
        elif self.__caixas[caixa_index] in None:
            print("fail: caixa vazio")
            return
        self.__caixas[caixa_index] = None

    def __str__(self, cliente=Cliente):
        caixa_str = [str(cliente) if cliente else "-----" for cliente in self.__caixas]
        fila_str = [str(cliente) for cliente in self.__fila]
        return f"Caixas: [{", ".join(caixa_str)}]\nEspera: [{", ".join(fila_str)}]"

def main():
    while True:
        cliente = Cliente
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "init":
            mercantil = Mercantil(int(args[1]))
        elif args[0] == "show":
            print(mercantil)
        elif args[0] == "arrive":
            nome = args[1]
            cliente = Cliente(nome)
            mercantil.addPessoa(cliente)
        elif args[0] == "call":
            mercantil.callCliente(int(args[1]))
        elif args[0] == "finish":
            mercantil.finish(int(args[1]))
        elif args[0] == "end":
            break
        else:
            print("fail:")

if __name__ == '__main__':
    main()