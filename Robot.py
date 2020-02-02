class Robot:
    '所有员工的基类'
    empCount = 0
    name = 'nobody'
    salary = 10

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Robot.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % self.empCount)

    def displayEmployee(self):
        print( "Name : ", self.name,  ", Salary: ", self.salary)