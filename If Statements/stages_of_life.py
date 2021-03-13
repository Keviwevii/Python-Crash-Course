#Determining age

age = 65

if age < 2:
    message = 'You are a baby!'
elif age < 4:
    message = 'You are a toddler!'
elif age < 13:
    message = 'You are a kid!'
elif age < 20:
    message= 'You are a teenager!'
elif age < 65:
    message = 'You are an adult!'
elif age >= 65:
    message = 'You are an elder!'
    
print(message)