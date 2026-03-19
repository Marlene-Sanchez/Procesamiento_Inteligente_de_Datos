class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    def pension(self):
        return self.years * .10 * self.salary

    def getname(self):
        return self.name


class Manager(Worker):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .20 * self.salary


class Executive(Manager):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .30 * self.salary


def main():
    workers = [Manager("Chris", 100000, 12),
               Executive("Susan", 100000, 7),
               Worker("Michael", 100000, 10)]

    fmt = "{:3} {:15.2f} {}"
    for idx, worker in enumerate(workers):
        print(fmt.format(idx, worker.pension(), worker.getname()))


if __name__ == "__main__":
    main()
