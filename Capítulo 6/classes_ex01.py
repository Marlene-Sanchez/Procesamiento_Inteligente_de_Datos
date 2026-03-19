#!/usr/bin/env python3


class Person:
    default = "Unknown"

    def __init__(self, name=default, age=1, gender=default):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


def main():
    mom = Person("Sally", 76, "F")
    dad = Person("Arthur", 62, "M")
    print(mom)
    print(dad)


if __name__ == "__main__":
    main()
