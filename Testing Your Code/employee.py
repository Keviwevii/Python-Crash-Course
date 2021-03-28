#Employee class to test

class Employee:
    '''Making a employee and addding to their salary.'''
    
    def __init__(self, first_name, last_name, salary):
        '''Initializing attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self, raise_amount=''):
        '''Adding money to the salary'''
        if raise_amount:
            self.salary += raise_amount
        else:
            self.salary += 5000  
        return self.salary
    
    def show_salary(self):
        '''Showing salary'''
        print(f'Your salary is {self.salary}')  
            
me = Employee('Kevin', 'Floyd', 50000)
me.show_salary()
me.give_raise()
me.show_salary()
