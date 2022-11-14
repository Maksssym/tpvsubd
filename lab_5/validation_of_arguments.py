class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

a = Figure("квадрат", 18)
print(a.type, a.length) 
b = Figure("прямокутник", 17)
print(b.type, b.length)
c = Figure("трикутник", 16)
print(c.type, c.length)