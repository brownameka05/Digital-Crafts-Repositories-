class Person:
    def __init__ (self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []


    def greet(self, other_person):
        print("Hello! {0}, I am {1}!" .format (other_person.name,self.name))

    def print_contact_info(self):
        print("My is email: {0}, my phone number: {1}" .format (self.email, self.phone))

    def other_person(self):
        print(self.friends)

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.email, self.phone)



Sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
Jordan = Person("Jordan","jordan@aol.com","495-586-3456")

Sonny.greet(Jordan)
Jordan.greet(Sonny)

Sonny.print_contact_info()
Jordan.print_contact_info()

Jordan.friends.append(Sonny)
print(Jordan.friends[0])

Sonny.friends.append(Jordan)
print(Sonny.friends[0])

print (len(Sonny.friends))

print (len(Jordan.friends))


print(Sonny.email,Sonny.phone)
print(Jordan.name,Jordan.email,Jordan.phone)


class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("car print_info")


car = Vehicle("Nissan", "Leaf", "2015")
car.print_info()
print(car.make,car.model,car.year)
