class Book:
    def getb(self):
        self.b_sub=input("Enter Book Subject :")
        self.b_title=input("Enter Book Title :")
        self.author=input("Enter Author :")
        self.pub=input("Enter Publisher Name :")
        self.isbn=input("Enter ISBN Number :")
        self.nc=input("Enter number of copies :")
        
    def displayb(self):
        print(f"Book Subject:{self.b_sub}\tBook Title:{self.b_title}\tBook Author:{self.author}\tBook Publisher:{self.pub}\tBook ISBN:{self.isbn}\tBook Copies{self.nc}")