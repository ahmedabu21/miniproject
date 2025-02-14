
courses=['Calculus','Cornerstone','Chemistry', 'Physics']
studentcourses=[]


def decision():
    dec=int(input("would you like to view (1), display(2) ,register (3), or exit (4)"))
    return dec

              
def view():
    print(courses)
    
def register():
    print(courses)
    for i in range(0,3):
        user_class = input("Enter course to add(MAX OF THREE")
        studentcourses.append(user_class)
        
        
        
    
    
def main():
   
    while True:
        try:
            if decision()==4:
                break
            elif decision()==1:
                view()
            elif decision==2:
                display()
                
            elif decision==3:
                register()
            
            
            
            
    
        except ValueError:
            print("h")
            
        

if __name__ == "__main__":
    main()