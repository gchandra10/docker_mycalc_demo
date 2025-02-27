from faker import Faker 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))

    fake = Faker() 
    print (fake.email()) 
    print(fake.country()) 
    print(fake.name()) 
    print(fake.text()) 
    print(fake.latitude(), fake.longitude()) 
    print(fake.url()) 