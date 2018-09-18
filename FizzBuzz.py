def FizzOrBuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")

number = int(input("Enter your number:"))
FizzOrBuzz(number)
