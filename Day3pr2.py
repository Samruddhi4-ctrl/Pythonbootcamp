class Student:
    #static data
    branch='CSE'
    def __init__(self,name,rollno,address,email,branch):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.email=email
    def display(self):
        print("name is:",self.name)
        print("roll no is:",self.rollno)
        print("address is:",self.address)
        print("email is:",self.email)
        print("branch is:",Student.branch)
s1=Student('sam',64,'hyderabad','sam@gmail.com','CSE')
s1.display()