"""
Module 5/7 consolidation — Jun 2023 P42 Q3 (33 marks): classes Employee and
Manager (inheritance, overriding SetPay with a bonus percentage); read
Employees.txt where a bonus line is present ONLY for managers (variable-length
records, so peek ahead); read HoursWeek1.txt and drive SetPay(); output every
employee's total pay.

Run:  python m07_employees.py

Data files: ../data-files/J23-42/Employees.txt and HoursWeek1.txt
(recreated in the paper's format)
"""

class Employee:
    # self.__HourlyPay     : REAL
    # self.__EmployeeNumber : INTEGER
    # self.__JobTitle      : STRING
    # self.__PayYear2022   : ARRAY[0:51] OF REAL
    def __init__(self, hourly_pay, employee_number, job_title):
        self.__HourlyPay = hourly_pay
        self.__EmployeeNumber = employee_number
        self.__JobTitle = job_title
        self.__PayYear2022 = [0.0 for _ in range(52)]   # 52 weeks, all 0.0

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, week_number, hours_worked):
        self.__PayYear2022[week_number - 1] = hours_worked * self.__HourlyPay

    def GetTotalPay(self):
        return sum(self.__PayYear2022)


class Manager(Employee):
    # self.__BonusValue : REAL   (a percentage)
    def __init__(self, hourly_pay, employee_number, bonus_value, job_title):
        super().__init__(hourly_pay, employee_number, job_title)
        self.__BonusValue = bonus_value

    def SetPay(self, week_number, hours_worked):
        # override: increase the hours by the bonus percentage, then delegate
        hours_worked = hours_worked * (1 + self.__BonusValue / 100)
        Employee.SetPay(self, week_number, hours_worked)


Employees = [None] * 8


def ReadEmployees():
    try:
        file = open("../data-files/J23-42/Employees.txt", "r")
        for i in range(8):
            hourly_pay = float(file.readline().strip())
            employee_number = int(file.readline().strip())
            next_line = file.readline().strip()
            try:
                # a bonus value parses as a number; a job title does not
                bonus = float(next_line)
                job_title = file.readline().strip()
                Employees[i] = Manager(hourly_pay, employee_number, bonus, job_title)
            except ValueError:
                Employees[i] = Employee(hourly_pay, employee_number, next_line)
        file.close()
    except Exception:
        print("File could not be opened")


def EnterHours():
    try:
        file = open("../data-files/J23-42/HoursWeek1.txt", "r")
        line = file.readline().strip()
        while line != "":
            employee_number = int(line)
            hours = float(file.readline().strip())
            for i in range(8):
                if Employees[i] is not None and Employees[i].GetEmployeeNumber() == employee_number:
                    Employees[i].SetPay(1, hours)   # polymorphic call
            line = file.readline().strip()
        file.close()
    except Exception:
        print("Hours file could not be opened")


def main():
    ReadEmployees()
    EnterHours()
    for i in range(8):
        if Employees[i] is not None:
            print(Employees[i].GetEmployeeNumber(),
                  "total pay:", round(Employees[i].GetTotalPay(), 2))


main()
