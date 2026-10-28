menu = """
======================================
=                title               = 
======================================
=         select from below          = 
= 1.) option 1                       =
= 2.) option 2                       =
= 3.) option 3                       = 
= 0.) quit                           =
=                                    =
=                                    =
======================================
""" 


#========== definitions ===============
def option1():
    print("Running option 1")
def option2():
    print("Running option 2")
def option3():
    print("Running option 3")


#=============== main =================
quit = False
while(1 == 1):
    print(menu)
    ans = input("Selection > ")
    if(quit): break
    if(ans == "0"): break
    elif(ans == "1"):
        option1()
    elif(ans == "2"):
        option2()
    elif(ans == "3"):
        option3()
    else:
        print("Invalid Input")
