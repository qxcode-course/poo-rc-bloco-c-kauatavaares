import random
class Foo:
    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return f"{self.num}"
    def __repr__(self):
        return str(self)

lista_int_vazia: list[int] = []
lista_obj_vazia: list[Foo] = []

lista_int:list[int] = [0 ,1, 2, 3, 4, 5]
lista_obj:list[Foo] = [Foo(1), Foo(2), Foo(3)]
print(len(lista_int))
print(len(lista_obj))

lista_int_vazia.append(6)
lista_obj.append(Foo(4))
print("Apos append:")
print(lista_obj)
print(lista_int_vazia)

lista_int.pop()
lista_obj.pop()
print("Apos o pop:")
print(lista_int)
print(lista_obj)

lista_int.insert(0, -1)
lista_obj.insert(0, Foo(5))
print("apos o insert:")
print(lista_int)
print(lista_obj)

lista_int.remove(2)
lista_obj.remove(lista_obj[2])
print("Apos o remove:")
print(lista_int)
print(lista_obj)

list_random_int:list[int] = [random.randint(0, 50) for _ in range(6)]
print("Random array:")
print(list_random_int)

list_sequencia:list[int] = list(range(10))
print("Sequencia de array:")
print(list_sequencia)

print("Acessando os elementos:")
print("Quinto numero:", list_sequencia[5])
print("Ultimo numero:", list_sequencia[-1])

print("Array como string(join by -):")
print("-".join(map(str, list_sequencia)))

list_sequencia_pares:list[int] = [x for x in list_sequencia if x % 2 == 0]
print("Array com elementos pares:")
print(list_sequencia_pares)

list_sequencia_quadrado: list[int] = [x ** 2 for x in list_sequencia_pares]
print("Array elevando eles ao quadrado:")
print(list_sequencia_quadrado)

list_sequencia.sort(reverse=True)
print("Array em ordem decrescente:")
print(list_sequencia)


num = int(input("Digite um numero para buscar na lista:"))
if num in list_sequencia:
    print(f"O numero {num} foi encontrado ")
else:
    print(f"O numero {num} nao foi encontrado")








