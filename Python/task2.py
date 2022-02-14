# Напиши класс Animal. Реализуй в нем любые 2 метода.
# Напиши класс Cat, который наследует класс Animal. Animal - родительский, 
# Cat - дочерний. Перекрой любой метод базового класса. Перекрытый метод 
# должен делать что-то свое, после чего вызывать метод родительского класса.


class Animal:

    def __init__(self, name):
        self.name = name

    def say(self):
        print("To say I do not know")

    def get_name(self):
        print(self.name)


class Cat(Animal):

    def say(self):
        print("myau!")


if __name__ == "__main__":
    cat = Cat("Barsik")
    cat.say()
    cat.get_name()
    Animal.say(cat)
    Animal.get_name(cat)

