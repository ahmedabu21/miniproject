
courses=['Calculus','Cornerstone','Chemistry', 'Physics']
studentcourses=[]


def decision():
    dec=int(input("would you like to view (1), display(2) ,register (3), or exit (4)"))
    return dec

def view():
    print("avalible courses to register:")
    for i in courses:
        print(i)


def display():
    print("You've registed for the folowing courses")
    for i in studentcourses:
        print(i)
       
def register():
    
    if len(studentcourses) <3:
        print(courses)
        user_course = input("Enter course to register: ")
        studentcourses.append(user_course)
        
    else:
        print("you cant register for more than three classes")

        
        
    

def main():
   
    while True:
        try:
            intdec=decision()
            
        
            if intdec==4:
                break

            elif intdec==3:
                register()
            elif intdec==2:
                display()
            elif intdec==1:
                view()
                
            else:
                print("enter a number 1-4")
            
            
            
            
    
        except ValueError:
            print("Enter a valid Option")
            
        

if __name__ == "__main__":
    main()