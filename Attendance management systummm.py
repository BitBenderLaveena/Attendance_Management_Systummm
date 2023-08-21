details={123:'naveen',124:'sachin',125:'seema'}
l=list([])
ch2='ongoing'

def add():
    eno=int(input("Enter your enrolment no"))
    name=input("Enter your name")
    details[eno]=name
    print("Sucessfully added")
def remove():
    eno=int(input("Enter your enrolment no"))
    del details[eno]
    print("Sucessfully removed")
def view():
    ch1=input("Enter whether a 'particular' student detail is to be viewd or 'total names' or 'total enrollment nos' or 'total' list")
    if ch1=='particular':
        eno=int(input("Enter eno of student"))
        print(details[eno])
    elif ch1=='total names':
        print(details.values())
    elif ch1=='total enrollment nos':
        print(details.keys())
    elif ch1=='total':
        print(details)
    else:
        print("Type correctly")
def update():
    eno=int(input("Enter the enrollment no whose name needs to be updated"))
    name=input("Enter the name to be updated")
    details[eno]=name
    print("Successfully Updated")
   
def markatt():
    ch3='yes'
    while ch3!='no':
        eno=int(input("Enter the enrollment no whose attendance needs to be marked"))
        if (eno in details):
            print("Present Marked successfully")
            l.append(eno)
        else:
            print("Not a student of class") 
        ch3=input("Enter no if no more attendence is to be marked as attend")    
def viewatt():
    ch4=input("Enter 'total' to get the list of enrollment no of total students present in the session or 'eno' to find a particular student using his enrollment no")
    
    if ch4=='total':
        print(l)
    elif ch4=='eno':
        enno=int(input("Enter the enrollment no of student"))
        res=print(enno in l)
        if res=='True':
            print("Student is present")
        else:
            print("Student is absent")
    else:
        print("Typing mistake")

def changeatt():
    ch5=input("Enter 'rem' to change presently marked attendance to absent ")
    if ch5=='rem':
        eno=int(input("Enter the enrollment no of student"))
        l.remove(eno)  
        print("Attendance changed Successfully")
    else:
        print("Typing mistake")    
    
cred=('admin',123)
c=5
for i in range(5):
    print("attempt left:",c)
    n=input("Enter your username:")
    p=int(input("Enter pwsd:"))
    if n==cred[0] and p==cred[1]:
        print("Successful login")
        
        while ch2!='stop':
            print("Choose your action")
            print("To add a new entry,choose 'ADD';To delete a previous entry,choose 'DEL';To view from current database,choose 'VIEW';To update a record ,choose 'UPDATE';To mark attendance,choose 'mark attendance';To view attendance,choose 'view attendance';To update attendance,choose 'change attendance"  )
            ch=input()
            if ch=='ADD':
                add()
            elif ch=='DEL':
                remove()
            elif ch=='VIEW':
                view()
            elif ch=='UPDATE':
                update()
            elif ch=='mark attendance':
                markatt()
            elif ch=='view attendance':
                viewatt()
            elif ch=='change attendance':
                changeatt()    
            else:
                print("Invalid choice")
            ch2=input("Enter 'stop' to exit ")
        break        
    else:
         print("Invalid choice,Try choice")
         c=c-1
 

