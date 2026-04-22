''' Class Deep diving
    (1) Encapsulation
    (2) Inheritence
    (3) Polymorphism
'''

print("======= INHERITENCE ===========")
# PARENT > CHILD [Parent class provides only public and protected properties to child classes!]


class Animal:  # Parant class
    # state
    description = "This class is parant for animals"

    # constructor
    def __init__(self, voice):
        self._status = " animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"The animal can make voice: {self.voice} ")


class Dog(Animal):
  # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

     # method
    def introduce(self):
        print(f"the {self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")


class Cat(Animal):
  # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

     # method
    def introduce(self):
        print(f"the {self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):
  # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

     # method
    def introduce(self):
        print(f"the {self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("=========")
dog.make_voice()
cat.make_voice()
fish.make_voice()

print("=========")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)
