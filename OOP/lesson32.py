class Employee:
    company="G" #class variable
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod
    def set_company(cls,new_company_name):
        cls.company=new_company_name # updates class variable

    @classmethod
    def get_value (cls, name, salary):
        return cls (name, int (salary)) # created an object so constructor starts
    
    def display_info(self): #instance method
        return f"Employee: {self.name}\nSalary: {self.salary}\nCompany: {self.company}"
    
emp1=Employee.get_value("F",1323) #in get_value object created so constructor start 
print(emp1.display_info())

Employee.set_company("M") # updates Employee.company for all instances 
emp2=Employee.get_value("S",2313)
print(emp2.display_info())