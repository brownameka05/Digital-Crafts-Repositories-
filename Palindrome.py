
input_word = input("Enter Word:")

if str(input_word) == str(input_word)[::-1]:
    print("True")
else:
    print("False")

print(input_word[::-1])
