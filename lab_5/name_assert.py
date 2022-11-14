class Name:
    def __init__(self, name) -> None:
        if name not in ["Максим", "Анонім"]:
            raise ValueError("Дозволені імена: Максим, Анонім")
        self.name = name

a = Name("Макс")