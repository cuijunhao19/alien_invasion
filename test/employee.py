class Employee:
    def __init__(self,first_name,last_name,yearly_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.yearly_salary=yearly_salary
        
    def give_raise(self,increase=5000):
        self.yearly_salary+=increase
        return self.yearly_salary
