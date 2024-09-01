  
class Employee:   # noun
    language = 'Py'   # class attribute
    salary = 1200000   # class attribute
    
    def getInfo(self):        
        print(f"language {self.language} and salary {self.salary}")

    def __init__(self, name, salary, language):    # this init is special method runs first as soon as object is created, its a constructor
        self.name = name
        self.salary = salary
        self.language = language

        print('i am creating an object', f"name: {name} salary: {salary} lang: {language}")

    @staticmethod
    def greet():     
        print("good morning")


harry = Employee("harry", 1300000, 'js')

print(harry.name)