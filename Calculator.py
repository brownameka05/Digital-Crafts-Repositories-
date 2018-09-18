def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if(choice == '1'):
    print(first_number, "+", second_number, "=", add(first_number, second_number))

elif(choice == '2'):
    print(first_number, "-", second_number, "=", subtract(first_number, second_number))

elif(choice == '3'):
    print(first_number, "*", second_number, "=", multiply(first_number, second_number))

elif(choice == '4'):
    print(first_number, "/", second_number, "=", divide(first_number, second_number))

else:
    print("Invalid")    
