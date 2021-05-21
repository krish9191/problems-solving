class Employee:
    def __init__(self, emp_id, name):
        self.id = emp_id
        self.name = name


class PayrollSystem:
    @classmethod
    def payroll_calculator(cls, Employee):
        for employee in Employee:
            print(f'Id:{employee.id}-{employee.name}')

            print(f'salary amount:{employee.payroll_calculator()}')


class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.salary = monthly_salary

    def payroll_calculator(self):
        return self.salary


class HourlyEmployees(Employee):
    def __init__(self, emp_id, name, no_of_hours, wage_per_hours):
        super().__init__(emp_id, name)
        self.hours = no_of_hours
        self.wage = wage_per_hours

    def payroll_calculator(self):
        return self.hours * self.wage


class CommissionEmployees(SalaryEmployee):
    def __init__(self, emp_id, name, monthly_salary, commission):
        super().__init__(emp_id, name, monthly_salary)
        self.commission = commission

    def payroll_calculator(self):
        fixed = super().payroll_calculator()
        return fixed + self.commission


if __name__ == '__main__':
    s = SalaryEmployee('00kt', 'Krishna', 5000)
    h = HourlyEmployees('00rp', 'Ramesh', 80, 25)
    c = CommissionEmployees('00sp', 'Santosh', 2000, 500)
    payroll = PayrollSystem()
    payroll.payroll_calculator([
        s, h, c
    ])
