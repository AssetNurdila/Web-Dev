from models import Dog, Cat

dog = Dog("Bobik", 3)
cat = Cat("Barsik", 2)

animals = [dog, cat]

for a in animals:
    print(a)
    print(a.info())
    print(a.speak())