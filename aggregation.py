class Department:
    def __init__(self,name):
        self.name = name
    def display_info(self):
        return f"Department:{self.name}"
class University:
    def __init__(self,name):
        self.name=name
        self.departments=[]
    def add_department(self,department):
        self.department.append(department)
    def diaplay_department(self):
        print(f"Departments in{self.name}University:")
        for department in self.department:
            print(department.display_info())

department1=Department("Computer Science")
department2=Department("Electrical Engineering ")
department3=Department("Mechanical Engineering")
university=University("Tech University")

university.add_department(department1)
university.add_department(department2)
university.add_department(department3)
university.display_departments()
