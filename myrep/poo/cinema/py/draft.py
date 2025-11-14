class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def getPhone(self) -> int:
        return self.phone
    def setPhone(self, phone: int):
        self.phone = phone
    def getId(self) -> str:
        return self.id
    def setId(self, id: str):
        self.id = id

    def __str__(self):
        return f"Id{self.id}, Phone{self.phone}"

class Theater:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats:list[Client | None]
    def