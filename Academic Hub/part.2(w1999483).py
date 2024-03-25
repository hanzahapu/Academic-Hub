# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1999483
 
# Date: 30 March 2023


#Define the variables

add1_star=""
add2_star=""
add3_star=""
add4_star=""
re_run= "y" 
add1=0
add2=0
add3=0
add4=0
list1=[]
list2=[]
list3=[]
list4=[]
 

#Getting the inputs 

def get_input():
    while True:
        try:
            global p_credit
            p_credit=int(input("\nPlease enter your credits at PASS: "))
            if p_credit not in [0,20,40,60,80,100,120]:
                print ("Out of range")
            else:
                break

        except ValueError:
            print("Integer required")

    while True:
        try:
            global d_credit  
            d_credit=int(input("Please enter your credit at DEFER: "))
            if d_credit not in [0,20,40,60,80,100,120]:
                print("out of range")
            else:
                break

        except ValueError:
            print("Integer required ")

    while True:
        try:
            global f_credit
            f_credit=int(input("Please enter your credits at FAIL: "))
            if f_credit not in [0,20,40,60,80,100,120]:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required ")

    global total 
    total=(p_credit+d_credit+f_credit)
    

#Calculation

def calculate():
    if total!=120:
        print("Total Incorrect")
        get_input()
        calculate()
    else:
        conditions()

#Making conditions

def conditions():
    if p_credit==120 and d_credit==0 and f_credit==0:
        print("Progress")
        global list1
        L=[p_credit,d_credit,f_credit]
        list1.append(L)
        global add1
        add1=add1+1
        global add1_star
        add1_star=add1_star+("*")

        
    elif p_credit==100 and d_credit<=20 and f_credit<=20:
        print ("Progresss (module trailer)")
        global list2
        L=[p_credit,d_credit,f_credit]
        list2.append(L)
        global add2
        add2=add2+1
        global add2_star
        add2_star=add2_star+("*")

        
    elif p_credit<=80 and d_credit<=120 and f_credit<=60:
        print("Do not progress - module retriever")
        global list3
        L=[p_credit,d_credit,f_credit]
        list3.append(L)
        global add3
        add3=add3+1
        global add3_star
        add3_star=add3_star+("*")

        
    elif p_credit<=40 and d_credit<=40 and (f_credit>=80 and f_credit<=120):
        print ("Exclude")
        global list4
        L=[p_credit,d_credit,f_credit]
        list4.append(L)
        global add4
        add4=add4+1
        global add4_star
        add4_star=add4_star+("*")

    repeat_run()    

#Repeat part
    
def repeat_run():
    re_run= input("\nEnter 'Y' for continue or 'q' to quit and view results: ").lower()
    choice= ['y','q']

    while re_run not in choice:
        print("Invalied Input! Only 'Q' or 'Y' Accepted")
        re_run= input("Enter 'y' for continue or 'q' to quit and view results: ").lower()

    if re_run== 'y':
            get_input()
            calculate()
            

    #Histogram


    elif re_run== 'q':
            print("\n---------------------------------------------------------------")
            print("\n")
            print("Histogram ")
            print("Progress ",add1,("     :"),add1_star)
            print("Trailer ",add2,("      :"),add2_star)
            print("Retriever ",add3,("    :"),add3_star)
            print("Exclude ",add4,("      :"),add4_star)
            print("\n\n")
            print((add1+add2+add3+add4),"Outcomes in total\n---------------------------------------------------------------")
            print("\n")
            print("Part2: ")
            print("\n")

            #Enter data to list
            
            if add1>=1:
                for a in range(0,len(list1),1):
                    print("Progress -                   ",str(list1[a:a+1])[2:-2])
            if add2>=1:
                for a in range(0,len(list2),1):
                    print("Progress (Module Trailer)-   ",str(list2[a:a+1])[2:-2])            
            if add3>=1:
                for a in range(0,len(list3),1):
                    print("Module Retriever -           ",str(list3[a:a+1])[2:-2])           
            if add4>=1:
                for a in range(0,len(list4),1):
                    print("Exclude -                    ",str(list4[a:a+1])[2:-2])



#start of the program
                    
get_input()
calculate()

  


