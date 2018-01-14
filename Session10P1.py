class student():
    def __init__(self, surname, lastname, studentnumber, course):
        self.surname = surname #Variable
        self.lastname = lastname #Variable
        self.studentnumber = studentnumber #Variable
        self.course = course #Variable

    def printDetails(self):
        

        print("Jack's surname is " +self.surname)
        print("Jack's last name is " +self.lastname)
        print("Jack's student number is " +self.studentnumber)
        print("Jack's course is " +self.course)
        
#this will get the variable that exists and return it when running
    def getSurname(self):
        return self.surname
    def getLastname(self):
        return self.lastname
    def getStudentnumber(self):
        return self.studentnumber
    def getCourse(self):
        return self.course
    
#this will set the new variable hence updating
    def setSurname(self, surnameinput):
        self.surname = surnameinput
    def setLastname(self, lastnameinput):
        self.lastname = lastnameinput
    def setStudentnumber(self, studentnumberinput):
        self.studentnumber = studentnumberinput
    def setCourse(self, courseinput):
        self.course = courseinput
