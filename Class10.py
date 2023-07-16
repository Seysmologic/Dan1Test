class A():

    def hello(self):
        print('Hello World!')
        return 2

    def bye(self):
        print('Bye!')
        return 1


class B(A):
    def _today(self):
        print('Date: 11.07.23')


class C(A):
    def next_day(self):
        print('Date: 12.97.23')

    @staticmethod
    def hello():
        print('Hello')


class D(B):
    pass


object1 = D()

print(object1.hello(), object1.bye())  # , object1.today())

print(object1._today())

print('&' * 50)
object2 = C()
print(object2.hello(), object2.bye(), object2.next_day(), object2.hello())


class Person(object):
    somet_attr = 'Person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __repr__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person1 = Person(name="John", age=30)

print(person1.name, person1.age)
print(person1)

person2 = Person('Person1', 25)
print(person2, person2.somet_attr)

person2.salary = 90000

print(person2.salary)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary} dollars.")

employee1 = Employee("Jane", 25, 50000)
employee1.say_hello()