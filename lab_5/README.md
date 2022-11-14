# Звіт до роботи
## Тема: Тестування програм
### Мета роботи: Тестування перевірки assert, робота з юніт тестами.
---
### Виконання роботи
- Результати виконання завдання *Lab_5*;
    1. Навчився виконувати перевірку assert, працювати з юніт тестами 
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті); 

![alt text](https://github.com/Maksssym/tpvsubd/blob/main/lab_5/Screenshots/name_assert.PNG "1")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/lab_5/Screenshots/number_assert.PNG "2")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/lab_5/Screenshots/validation_of_arguments.PNG "3")

- вставлений код / текстовий або числовий результат / інші результати:
Перевірка assert:
```python
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")

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

class Name:
    def __init__(self, name) -> None:
        if name not in ["Максим", "Анонім"]:
            raise ValueError("Дозволені імена: Максим, Анонім")
        self.name = name

a = Name("Макс")
```

### Висновок: 
- :question: Що зроблено в роботі; - Додавання бібліотек та робота з ними
- :question: Чи досягнуто мети роботи; - Досягнуто
- :question: Які нові знання отримано; - Робота з Python 
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; - Так
- :question: Чи вдалося виконати всі завдання; - Так
- :question: Чи виникли складності у виконанні завдання; - Ні
- :question: Чи подобається такий формат здачі роботи (Feedback); - Більше так, ніж ні
- :question: Побажання для покращення (Suggestions); - Немає
---