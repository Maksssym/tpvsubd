# Звіт до роботи
## Тема: Перша програма на Python
### Мета роботи: Навчитись створювати програми на Python
---
### Виконання роботи
- Результати виконання завдання *Lab_2*;
    1. Навчився створювати 8 нових програм на Python, вивчив новий матеріал. 
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті); 

![alt text](https://github.com/Maksssym/tpvsubd/blob/main/2.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")
![alt text](https://github.com/Maksssym/tpvsubd/blob/main/1lab.PNG "code result")

- вставлений код / текстовий або числовий результат / інші результати:
```python
a = "змінна з текстом"
b = 1 # числова Змінна
c = ["a", 1, 1.25, "Слово"] # List
d = {"a": "Слово", "b": 1} # Dict
e = ("a", ) # Tuple
f = {"ss", } # Set

print("Перша константа", False)

print(abs(-14.1), f"є рівним {abs(14.1)}")

letters = ["m", "a", "x"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

B = True
print("Значить B=True" if B else "Значить B=False")

B = 0
try:
    print("Що буде якщо", 10/B, "?")
except Exception as e:
    print(e)
finally:
    print("А ось в чому справа!")

with open("README.md", "r") as f:
    for line in f:
        print(line)

this_is_lambda = lambda first, last: f'Максим сьогодні прокинувся о: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('7', 'ранку'))
```

### Висновок: 
- :question: Що зроблено в роботі; - 8 програм на Python
- :question: Чи досягнуто мети роботи; - Досягнуто
- :question: Які нові знання отримано; - Робота з GitHub та Python 
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; - Так
- :question: Чи вдалося виконати всі завдання; - Так
- :question: Чи виникли складності у виконанні завдання; - Ні
- :question: Чи подобається такий формат здачі роботи (Feedback); - Більше так, ніж ні
- :question: Побажання для покращення (Suggestions); - Немаe
---