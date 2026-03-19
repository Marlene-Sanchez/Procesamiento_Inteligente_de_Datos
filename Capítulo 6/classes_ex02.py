
class Person:
    default = "Unknown"

    def __init__(self, name=default, age=1, gender=default):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


class Family:
    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.kids = list(children)

    def add(self, child):
        self.kids.append(child)

    def __str__(self):
        family = str(self.parent1) + " " + str(self.parent2)
        for kid in self.kids:
            family += "\n\t" + str(kid)
        return family


def main():
    mom = Person("Sally", 76, "F")
    dad = Person("Arthur", 62, "M")
    print(mom, dad)

    joel = Person("Joel", 41, "M")
    judy = Person("Judy", 38, "F")
    fam = Family(mom, dad, joel, judy)
    print("*** Family Members are")
    print(fam)
    print()
    mike = Person("Michael", 33, "M")
    fam.add(mike)
    print("*** Family Members are")
    print(fam)


if __name__ == "__main__":
    main()
