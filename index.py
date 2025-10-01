## Task 1 File to List Converter ##

filename = input("Skriv inn filnavn: ") #rompt the user for a filename.

try:
    with open(filename, "r") as f: #Read all lines from the file into a list.
        lines = [line.strip() for line in f.readlines()] #Strip whitespace from each line and print the resulting list.
    print(lines)
except FileNotFoundError:
    print("Feil: Filen finnes ikke.") #Handle the case where the file doesn't exist using try/except and print an error message.

## Task 3 Simple Class and Inheritance ##

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hei, jeg heter {self.name} og er {self.age} år gammel.") #Define a Person class that has attributes name and age and a method greet() that prints a greeting.


class Student(Person):
    def __init__(self, name, age, student_id): #Define a Student class that inherits from Person and adds an attribute student_id.
        super().__init__(name, age)
        self.student_id = student_id


# In your main script, create a Student object and call its greet() method.
student = Student("Anna", 22, "S12345")
student.greet()
print("Student-ID:", student.student_id) #Print the student's student_id as well.

## Task 4 Math Quiz with Exception Handling ##

import random #Use the random module (from the standard library) to generate two random integers and ask the user to add them.

a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"Hva er {a} + {b}?")

try:
    answer = int(input("Svar: "))
    if answer == a + b:
        print("Riktig!")
    else:
        print("Feil, riktig svar er:", a + b) #If the input is valid, check if the answer is correct and print a message accordingly.
except ValueError:
    print("Invalid input!") #Try to convert the user's input to an integer. If that fails (e.g., user enters non-digit input), handle the exception and print "Invalid input!".

## Task 7 Scoped Variables Experiment ## 

def outer_function():
    x = "inne i outer_function"
    print("Outer:", x) #Write a function that defines a variable inside it, and print it.

    def inner_function():
        x = "inne i inner_function" #Outside the function, define a variable with the same name and a different value, and print it.
        print("Inner:", x) 
    inner_function()

    for i in range(1):
        x = "inne i loop"
        print("Loop:", x) #Call the function and print again to show scope differences.


x = "utenfor funksjoner"
print("Global:", x) #Add another nested function or loop to show how scope changes in that context as well.

outer_function()

print("Global etter kall:", x)

## Task 9 File Filtering and Writing ##

filename = input("Skriv inn filnavn: ")
keyword = input("Skriv inn nøkkelord: ") #Ask the user for a filename and a keyword.

try:
    with open(filename, "r") as f:
        lines = f.readlines()

    matches = [line for line in lines if keyword in line] #Read the file line-by-line and select only the lines containing the keyword.

    with open("filtered.txt", "w") as out:
        out.writelines(matches) #Write these matching lines to a new file filtered.txt.

    print(f"{len(matches)} linjer skrevet til filtered.txt")
except FileNotFoundError:
    print("Feil: Filen finnes ikke.")
except IOError:
    print("Feil ved lesing eller skriving av fil.") #Handle any file read/write errors, printing a friendly error message if something goes wrong.
