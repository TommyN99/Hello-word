from Session10p1 import student
def main():
    jack = student("Jones","Daniel","213","Maths")
    jack.printDetails()

    jack.setSurname("Daves")
    jack.printDetails()

    answer = jack.getSurname()+ " studentnumber = "+jack.getStudentnumber()
    print (answer)
    
main()
