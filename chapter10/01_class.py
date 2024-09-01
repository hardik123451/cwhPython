#  1 class,   2  attributes    3 self 

def getSurname():
    print("hi")
    
class Employee:   # noun
    language = 'Py'   # class attribute
    salary = 1200000   # class attribute
    surname = getSurname()  #verbs  methods

    def __init__(self):  # dunder method which is automatically called 
        print("i am creating the object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod    
    def greet():
        print("good morning")


harry = Employee()
harry.name = "harry"     # added  object attribute // instance attribute   // program first checks instance attribute present or not otherwise it prints class attributes value
print(harry.name, harry.language)
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)









