# Звіт до роботи
## Тема: Перша програма на Python
### Мета роботи: Навчитись створювати програми на Python
---
### Виконання роботи
- Результати виконання завдання *Lab_3*;
    1. Розробив програму на Python
    1. Навчився створювати програму на Python
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті); 

![alt text](https://github.com/Maksssym/tpvsubd/blob/main/lab_1/1lab.PNG "code")

- вставлений код / текстовий або числовий результат / інші результати:
```python
class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self): 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"


print("Let's Start!")

names = ("Maksym", "Ostap", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")
print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

```

### Висновок: 
- :question: Що зроблено в роботі; - Програму на Python
- :question: Чи досягнуто мети роботи; - Досягнуто
- :question: Які нові знання отримано; - Робота з GitHub та Python 
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; - Так
- :question: Чи вдалося виконати всі завдання; - Так
- :question: Чи виникли складності у виконанні завдання; - Ні
- :question: Чи подобається такий формат здачі роботи (Feedback); - Більше так, ніж ні
- :question: Побажання для покращення (Suggestions); - Немаe
---