#Modifying out User class

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
        
#Create an instance and test login attempt methods
kevin = User('Kevin', 'Floyd', 25, 151)
kevin.describe_person()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
print(f'Login attempts: {kevin.login_attempts}')
kevin.reset_login_attempts()
print(f'Login attempts: {kevin.login_attempts}')
