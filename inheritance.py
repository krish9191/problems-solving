

class Employees:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class Payrollsystem:
    def payroll_calculator(self,Employees):
        for employee in Employees:
            print(f'Id:{employee.id}-{employee.name}')

            print(f'salary amount:{employee.payroll_calculator()}')

class Salaryemployees(Employees):
    def __init__(self,id,name,monthly_salary):
        super().__init__(id,name)
        self.salary=monthly_salary
    def payroll_calculator(self):
        return self.salary

class Hourlyemployees(Employees):
    def __init__(self,id,name,no_of_hours,wage_per_hours):
        super().__init__(id,name)
        self.hours=no_of_hours
        self.wage=wage_per_hours
    def payroll_calculator(self):
        return self.hours*self.wage

class Commissionemployees(Salaryemployees):
    def __init__(self,id,name,monthly_salary,commision):
        super().__init__(id,name,monthly_salary)
        self.commission=commision
    def payroll_calculator(self):
        fixed=super().payroll_calculator()
        return fixed+self.commission

if __name__=='__main__':
    s=Salaryemployees('00kt','krishna',5000)
    h=Hourlyemployees('00rp','ramesh',80,25)
    c=Commissionemployees('00sp','sagar',2000,500)
    payroll=Payrollsystem()
    payroll.payroll_calculator([
        s, h,c
    ])








