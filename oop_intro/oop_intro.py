class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        # Якщо ім'я не передали (None) - беремо ім'я з "анонімного" об'єкта
        self.name = name if name is not None else self.anonymous_user().name

        # Перевірка: лише літери
        if not self.name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        # Перша літера завжди велика (решту літер не змінюємо)
        self.name = self.name[0].upper() + self.name[1:]

        MyName.total_names += 1  # modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
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

    @property
    def full_name(self) -> str:
        """Class property
        return: "User #<id>: <name> (<email>)"
        """
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Instance method
        domain: значення після @ (можна змінити)
        """
        return f"{self.name}@{domain}"

    def count_letters(self) -> int:
        """Instance method: кількість букв в імені
        """
        return len(self.name)

    def save_to_file(self, filename="users.txt") -> None:
        """Instance method: додає рядок із записом у файл
        """
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "Danylo")  # додано своє ім'я
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


# ---------------------- Індивідуальні завдання ----------------------
print("\n--- Індивідуальні завдання ---")

# 2. Інший текст привітання
print(MyName.say_hello("Привіт, студенте!"))

# 3. Кількість букв в імені
for me in all_names.values():
    print(f"{me.name}: {me.count_letters()} літер(и)")

# 4. Порівняння кількості імен
print(f"Імен у списку names: {len(names)}, лічильник класу: {MyName.total_names}")

# 5. Перша літера завжди велика
print(MyName("danylo").name)

# 6. Інший домен після @
print(all_names["Danylo"].create_email("gmail.com"))

# 7. Перевірка на цифри/символи
for bad_name in ("Dan1lo", "Max!"):
    try:
        MyName(bad_name)
    except ValueError as error:
        print(f"{bad_name}: ValueError - {error}")

# 8. full_name
print(all_names["Danylo"].full_name)

# 9. Запис у файл
for me in all_names.values():
    me.save_to_file()
print("Користувачів збережено у users.txt")
