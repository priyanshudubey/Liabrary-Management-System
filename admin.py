import pickle
from Books import *
from Faculty import *
from students import *

class admin:
    
#**********************************************************************************************************
    def add_book(self):
        with open("book.pkl","ab") as f:
            l=[]
            n=int(input("How many Books to you want to add :"))
            print("\n")
            for i in range(n):
                print(f"\n\tEnter Record of Book {i+1}:-")
                b=Book()
                b.getb()
                l.append(b)
            pickle.dump(l,f)
            print("Book Record added successfully")
#***********************************************************************************************************
    def display_book(self):
        with open("book.pkl",'rb') as f:
            print(f"\nBOOK RECORD:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.displayb()
                except EOFError:
                    print("Data read is completed")
                    break

#************************************************************************************************************
    def remove_book(self):
        obj=None
        with open("book.pkl","rb") as f:
            bn=input("\nEnter the ISBN number or book title to completely remove the book : ")
            k=0
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.b_title == bn or i.isbn == bn:
                            obj.remove(i)
                            k=1
                except EOFError:
                    if(k==1):
                        print("Book is removed")
                    else:
                        print("\nBook not found")
                    break
        with open("book.pkl","wb") as f:
            pickle.dump(obj,f)

#**************************************************************************************************************
    def add_student(self):
        with open("student.pkl","wb") as f:
            l=[]
            n=int(input("How many Students you want to add in record :"))
            print("\n")
            for i in range(n):
                print(f"\n\tEnter Record of Student {i+1}:-")
                b=Students()
                b.gets()
                l.append(b)
            pickle.dump(l,f)
            print("Student Record added successfully")
            
#*********************************************************************************************
    def display_student(self):
        with open("student.pkl",'rb') as f:
            print(f"\tSTUDENT RECORD:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.display()
                except EOFError:
                    print("Data read is completed")
                    break
#*********************************************************************************************
    def remove_student(self):
        obj=None
        with open("student.pkl","rb") as f:
            bn=input("\nEnter the Enrollment Number to completely remove the student record : ")
            k=0
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll == bn:
                            obj.remove(i)
                            k=1
                except EOFError:
                    if(k==1):
                        print("Student record is removed")
                    else:
                        print("\nStudent record not found")
                    break
        with open("student.pkl","wb") as f:
            pickle.dump(obj,f)

#*********************************************************************************************
    def add_faculty(self):
        with open("faculty.pkl","wb") as f:
            l=[]
            n=int(input("How many Faculty record you want to add :"))
            print("\n")
            for i in range(n):
                print(f"\n\tEnter Record of Faculty {i+1}:-")
                b=Faculty()
                b.getf()
                l.append(b)
            pickle.dump(l,f)
            print("Student Record added successfully")
            
#*********************************************************************************************
    def display_faculty(self):
        with open("faculty.pkl",'rb') as f:
            print("\nFaculty Record:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        i.displayf()
                except EOFError:
                    print("Data read is completed")
                    break
#*********************************************************************************************
    def remove_faculty(self):
        obj=None
        with open("faculty.pkl","rb") as f:
            bn=input("\nEnter the Faculty ID to completely remove the faculty record : ")
            k=0
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.eid == bn:
                            obj.remove(i)
                            k=1
                except EOFError:
                    if(k==1):
                        print("Faculty record is removed")
                    else:
                        print("\nFaculty record not found")
                    break
        with open("faculty.pkl","wb") as f:
            pickle.dump(obj,f)
            
#*********************************************************************************************************************************

    def issue_book_student(self):
        with open("book.pkl","rb") as f:
            bn=input("\nEnter the ISBN number of book : ")
            while (1):
                try:
                    l=[]
                    z=0
                    z1=0
                    obj=pickle.load(f)
                    for i in obj:
                        z1+=1
                        if i.isbn==bn:
                            if i.nc != 0:
                                i.nc=int(i.nc)-1
                                with open("issue_book.pkl","ab") as g:
                                    l.append(i.isbn)
                                    l.append(i.b_title)
                                    with open("student.pkl","rb") as h:
                                        kn=input("\nEnter your enrollment number:")
                                        while(1):
                                            try:
                                                abj=pickle.load(h)
                                                for j in abj:
                                                    if j.enroll==kn:
                                                        l.append(j.enroll)
                                                        l.append(j.name)
                                                        t=date.today()
                                                        k=int(input("Enter number of days after which you want to return book:"))
                                                        t+=timedelta(k)
                                                        l.append(t)
                                            except EOFError:
                                                break
                                    pickle.dump(l,g)
                            else:
                                print("No Book Copies left to issue")
                        else:
                            z+=1
                    if (z==z1):
                        print("Book ISBN error")
                except EOFError:
                    break
#*************************************************************************************************************************************              
    def display_issued_book_student(self):
        with open("issue_book.pkl",'rb') as f:
            print("\nIssued Book Record:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    print(f"Book ISBN:{obj[0]}\tBook Title:{obj[1]}\tStudent Enrollment:{obj[2]}\tStudent Name:{obj[3]}\tDue Date:{obj[4]}")
                except EOFError:
                    break        
#*********************************************************************************************************************************

    def check_fine(self):
        bn=input("Enter your enrollment number:")
        with open("issue_book.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if(bn==obj[2]):
                        t=date.today()
                        l=t-obj[4]
                        if(l.days>0):
                            print(f"Book:{obj[1]}\tYour Fine is rupees:{l.days*0.50}")
                        else:
                            print(f"Book:{obj[1]}\tNo fine")
                except EOFError:
                    break
#****************************************************************************************************************************************

    def issue_book_faculty(self):
        with open("book.pkl","rb") as f:
            bn=input("\nEnter the ISBN number of book : ")
            while (1):
                try:
                    l=[]
                    z=0
                    z1=0
                    obj=pickle.load(f)
                    for i in obj:
                        z1+=1
                        if i.isbn==bn:
                            if i.nc != 0:
                                i.nc=int(i.nc)-1
                                with open("issue_book_faculty.pkl","wb") as g:
                                    l.append(i.isbn)
                                    l.append(i.b_title)
                                    with open("faculty.pkl","rb") as h:
                                        kn=input("\nEnter your Faculty Id:")
                                        while(1):
                                            try:
                                                abj=pickle.load(h)
                                                for j in abj:
                                                    if j.eid==kn:
                                                        l.append(j.eid)
                                                        l.append(j.name)
                                                        t=date.today()
                                                        k=int(input("Enter number of days after which you want to return book:"))
                                                        t+=timedelta(k)
                                                        l.append(t)
                                            except EOFError:
                                                break
                                    pickle.dump(l,g)
                            else:
                                print("No Book Copies left to issue")
                        else:
                            z+=1
                    if (z==z1):
                        print("Book ISBN error")
                except EOFError:
                    break
#***************************************************************************************************************************************                  
    def display_issued_book_faculty(self):
        with open("issue_book_faculty.pkl",'rb') as f:
            print("\nIssued Book Record:-")
            print("***************************************************************************************")
            while (1):
                try:
                    obj=pickle.load(f)
                    print(f"Book ISBN:{obj[0]}\tBook Title:{obj[1]}\tFaculty Id:{obj[2]}\tFaculty Name:{obj[3]}\tDue Date:{obj[4]}")
                except EOFError:
                    break
                    
#*********************************************************************************
    def return_book(self):
        bn=input("Enter Enrollment Number;")
        kn=input("Enter Book ISBN Number")
        with open("issue_book.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        if obj[0]==kn:
                            t=date.today()
                            l=t-obj[4]
                            if l.days<=0:
                                print("Book Return Successful")
                                obj=None
                            else:
                                print("You need to pay fine first")
                except EOFError:
                    break
        with open("issue_book.pkl",'wb') as f:
            pickle.dump(obj,f)
                    
#*********************************************************************************
    def renew_book(self):
        bn=input("Enter Enrollment Number:")
        kn=input("Enter Book ISBN Number:")
        with open("issue_book.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        if obj[0]==kn:
                            t=date.today()
                            l=t-obj[4]
                            if l.days<=0:
                                k=int(input("Enter days after which you want to return:"))
                                obj[4]+=timedelta(k)
                            else:
                                print("You need to pay fine first")
                except EOFError:
                    break
        with open("issue_book.pkl",'wb') as f:
            pickle.dump(obj,f)
            
#*********************************************************************************
    def return_book_faculty(self):
        bn=input("Enter Faculty Id")
        kn=input("Enter Book ISBN Number")
        with open("issue_book_faculty.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        if obj[0]==kn:
                            print("Book Return Successful")
                            obj=None
                except EOFError:
                    break
        with open("issue_book_faculty.pkl",'wb') as f:
            pickle.dump(obj,f)
                    
#*********************************************************************************
    def renew_book_faculty(self):
        bn=input("Enter Faculty Id:")
        kn=input("Enter Book ISBN Number:")
        with open("issue_book_faculty.pkl",'rb') as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    if obj[2]==bn:
                        if obj[0]==kn:
                            k=int(input("Enter days after which you want to return:"))
                            obj[4]+=timedelta(k)
                except EOFError:
                    break
        with open("issue_book_faculty.pkl",'wb') as f:
            pickle.dump(obj,f)