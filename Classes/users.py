#User Class

class User:
    
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        
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
 
#Creating instances and calling both methods        
kevin = User('Kevin', 'Floyd', 25, 151)
kevin.describe_person()
kevin.greet_user()