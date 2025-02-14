
courses=['Calculus','Cornerstone','Chemistry', 'Physics']
studentcourses=[]


def decision():
    dec=int(input("would you like to view (1), display(2) ,register (3), or exit (4)"))
    return dec
              


def display():
    print("You've registed for the folowing courses")
    for i in studentcourses:
        print(i)
       
    
    
    
#def check():
    
def main():
   
    while True:
        decision()
        try:
            intdec=decision()
            
        
            if intdec==4:
                break
            elif intdec==1:
                view()
            elif intdec==2:
                display()
            
            elif intdec==3:
                register()
            
            
            
            
    
        except ValueError:
            print("h")
            
        

if __name__ == "__main__":
    main()