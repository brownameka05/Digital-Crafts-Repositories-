number = int(input("Enter your number:"))

if number > 1:
    for index in range(2,number):
        if (number % index) == 0:
            print(number, "Not A Prime")
            break
    else:
        print(number, "Prime")
