import pickle
class Faculty:
    
    def getf(self):
        self.name=input("Enter name :")
        self.eid=input("Enter Faculty Id :")
        self.dp=input("Enter Department :")
        self.ph=input("Enter Phone number :")

        
    def displayf(self):
        print(f"Name :{self.name}\tFaculty Id :{self.eid}\tDepartment : {self.dp}\tPhone number : {self.ph}")
   
    def profile(self):
        bn=input("Enter your Faculty Id to display your profile:")
        with open("faculty.pkl",'rb') as f:
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.eid==bn:
                            print("YOUR PROFILE:-")
                            print("**************************************")
                            i.displayf()
                except EOFError:
                    break
                    
    def View_issued_book(self):
        bn=input("Enter your Faculty Id:")
        with open("issue_book_faculty.pkl",'rb') as f:
            while (1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        print(f"Book ISBN:{obj[0]}\tBook Title:{obj[1]}\tDue Date:{obj[4]}")
                except EOFError:
                    break
                    
    def display_book(self):
        with open("book.pkl",'rb') as f:
            print(f"\nBook Subject\tBook Title\tBook Author\tBook Publisher\tISBN number\tNumber of Copies")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.displayb()
                except EOFError:
                    print("Data read is completed")
                    break
    