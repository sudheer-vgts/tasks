import sqlite3
con=sqlite3.connect('school.db')
try:
    con.execute('''CREATE TABLE Students
            (REGNO INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
            CLASS_SECTION INTEGER NOT NULL,
            NAME   TEXT    NOT NULL,
            ADDRESS   TEXT,
            FOREIGN KEY(CLASS_SECTION) REFERENCES Sections(ID))''')
    
    
except Exception as e:
    print(e)

try:
    con.execute('''CREATE TABLE Sections 
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    CLASSNO INTEGER NOT NULL,
    SECTION TEXT)''')
except Exception as e:
    print(e)

cur=con.cursor()
class Student():
    def __init__(self,classno,regno,name,address):
        self.classno=classno
        self.regno=regno
        self.name=name
        self.address=address

    

    def create(self):
        cur.execute("INSERT INTO Students(CLASS_SECTION,NAME,ADDRESS) VALUES ("+str(self.classno)+",'"+self.name+"','"+self.address+ "')")
        con.commit()
        return cur.lastrowid

    def update(self):
        n="UPDATE Students SET NAME='"+self.name+"',CLASSNO="+str(self.classno)+",ADDRESS='"+self.address+"'WHERE REGNO="+str(self.regno)
        cur.execute(n)
        con.commit()
        return cur.fetchall

    def delete(regno):
        cur.execute("DELETE FROM Students WHERE REGNO="+str(regno))
        con.commit()
        return True

    def view(cls):
        res=con.execute("Select * from Students where CLASS_SECTION="+str(cls))
        print("class ID :"+str(cls))
        if res.arraysize==0:
            print("No students in this class")
        else:
            print("___________________________________\n")
            for i in res:
                print("Student Regno is "+str(i[0]))
                print("Student Name is "+i[2])
        
                class_id=con.execute("SELECT * from Sections where id="+str(i[1]))
                for j in class_id:
                    print("Student class is "+str(j[1]))
                    print("Student section is "+str(j[2]))
                print("Student address is "+i[3])
                print("____________________________________\n")


    def viewAll():
        res=con.execute("Select DISTINCT CLASS_SECTION from Students")
        if res.arraysize==0:
            print("No students in school")
        else:
            for i in res:
                if i is not None:
                    Student.view(i[0])

    def get_student(regno):
        res=cur.execute("SELECT * from Students WHERE REGNO="+str(regno))
        for i in res:
            return i
       
def sections():
    res=con.execute("SELECT * from Sections")
    print("   Classno|Section")
    print("------------------")
    for i in res:
        print(str(i[0])+".    "+str(i[1])+"  -  "+i[2])

while True:
    print("\n---------------------------")
    print("0.Exit\n1.Create\n2.Update\n3.Delete\n4.View Students in class\n5.View all student\n6.Student Details")
    print("---------------------------\n")
    ch=int(input("Enter your choice :"))

    if ch==0:
        break

    elif ch == 1:
        name=input("Enter the student name :")
        address=input("Enter the student address :")
        sections()
        classno=int(input("Enter the ID of class :"))
        std=Student(classno=classno,name=name,address=address,regno=None,)
        print("Regno is "+str(std.create()))
 
    elif ch==2:
        regno=int(input("Enter the Regno. :"))
        if Student.get_student(regno) is not None:
            sections()
            classno=int(input("Enter the ID of class :"))
            name=input("Enter the student name :")
            address=input("Enter the student address :")
            std=Student(classno=classno,name=name,address=address,regno=regno,)
            print("Regno is "+str(std.update()))
        else:
            print("No student found with regno "+str(regno))

    elif ch==3:
        regno=int(input("Enter the Regno. :"))
        if Student.get_student(regno) is not None:
            Student.delete(regno)
        else:
            print("No student found with regno "+str(regno))

    elif ch == 4:
        sections()
        classno=int(input("Enter the ID of class :"))
        std=Student.view(classno)

    elif ch == 5:
        Student.viewAll()

    elif ch == 6:
        regno=int(input("Enter the Regno. :"))
        i=Student.get_student(regno)
        print("____________________________________\n")
        print("Student Regno is "+str(i[0]))
        print("Student Name is "+i[2])
        class_id=con.execute("SELECT * from Sections where id="+str(i[1]))
        for j in class_id:
            print("Student class is "+str(j[1]))
            print("Student section is "+str(j[2]))
        print("Student address is "+i[3])
        print("____________________________________\n")

  
        
            

    #elif ch==8:
    #    for i in range(1,8):
    #        for j in ["A","B"]:
    #            con.execute("INSERT INTO Sections(CLASSNO,SECTION) VALUES("+str(i)+",'"+j+"')")
    #            con.commit()
    #            

    else:
        print("Invalid")
