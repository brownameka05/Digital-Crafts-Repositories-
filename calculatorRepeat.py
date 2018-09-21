def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation.")
print("+")
print("-")
print("*")
print("/")
print("q for Q")

while True:
    try:

        choice = input("Enter choice(+/-/*///q for Quit):")
        if(choice == 'q'):
            print("Bye")

        first_number = input("Enter first number:")
        if(first_number == 'q'):
            break
        first_number_real = int(first_number)


        second_number = input("Enter second number: ")
        if(second_number == 'q'):
            break
        second_number_real = int(second_number)

        if(choice == '+'):
            print(first_number_real, "+", second_number_real, "=", add(first_number_real, second_number_real))

        elif(choice == '-'):
            print(first_number_real, "-", second_number_real, "=", subtract(first_number_real, second_number_real))

        elif(choice == '*'):
            print(first_number_real, "*", second_number_real, "=", multiply(first_number_real, second_number_real))

        elif(choice == '/'):
            print(first_number_real, "/", second_number_real, "=", divide(first_number_real, second_number_real))
        else:
            print ("start again")

    except ValueError:
        print("Input a number")
