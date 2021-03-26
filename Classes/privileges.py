#Making a seperate class for privileges from admin.py

class User:
    
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.login_attempts = 0
        
    def describe_person(self):
        print(
            f'''Loading Information.....
First name: {self.first_name}
Last name: {self.last_name}
Age: {self.age}
Weight: {self.weight}'''
        )
    
    def greet_user(self):
        print(f'Greetings {self.first_name} {self.last_name}!')
        
    def increment_login_attempts(self):
        '''Increases the number of login attempts'''
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        '''Resets login attempts'''
        self.login_attempts = 0

#Making privileges its own class        
class Privileges:
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        print('As an admin you have the following privileges: ')
        for privileges in self.privileges:
            print(privileges.upper())
 
#Using inheritance to make a admin class        
class Admin(User):
    
    def __init__(self, first_name, last_name, age, weight):
        '''Initialize parent attributes'''
        super().__init__(first_name,last_name,age,weight)
        self.privileges = Privileges() #Setting our privileges attrivute to the instance
        

new_admin = Admin('Janet', 'Jackson', 24, 130)
new_admin.privileges.show_privileges()