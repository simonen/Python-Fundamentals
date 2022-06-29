class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last} {self.email}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(", ")
        return cls(first, last, pay)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        pass


emp_str_1 = 'John, Doe, 70000'
emp_str_2 = 'Stevie, Perkins, 10000'
emp_str_3 = 'Jane, Dodson, 20000'
dev1 = Developer('Cory', 'Chase', '30000')
new_emp_2 = Employee.from_string(emp_str_2)

print(dev1.__dict__)
