#CHAMATH DIKLSHAN MAHAPATUNA
#w1902042
#Importing functions from diffrent files
from Horizontal_histogram import Horizontal_histogram
from write_data import write_data
from Vertical_histogram import Vertical_histogram

#variable initialization
list2 = [0, 20, 40,60, 80, 100, 120 ]
Progress =0
Trailer =0
Exclude=0
Retriever=0
list1= []
loop1 = True
loop2 = True
loop3 = True
loop4 = True
Outcomes = 0

#function for user input
def validate_input(MarkType):
    global passMarks
    global defer
    global fail
    isValidated = True
    while isValidated:
        try:
            if MarkType == "pass":
                credit = input("Please enter your credits at pass ")
            elif MarkType == "defer":
                credit = input("Please enter your credits at defer ")
            elif MarkType == "fail":
                credit = input("Please enter your credits at fail ")
            marks = int(credit)
            if marks in list2:
                isValidated = True
                return credit
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
       
        
              
def calculateRank():
    global Progress
    global Trailer
    global Exclude
    global Retriever
    global Outcomes
    if total_marks == 120 and int(passMarks) == 120:
        Progress = Progress+1
        Outcomes = Outcomes+1
        return "Progress"
    elif total_marks == 120 and int(passMarks) == 100:
        Trailer = Trailer+1
        Outcomes = Outcomes+1
        return "module trailer"
    elif total_marks == 120 and int(deferMarks)>=0 and int(failMarks)<=60:
        Retriever = Retriever+1
        Outcomes = Outcomes+1
        return "module retriever"
    else:
        if total_marks == 120 :
            Exclude = Exclude+1
            Outcomes = Outcomes+1
            return "Exclude"


#calculation Part & d display the appropriate progression for each individual student      
def main():
    global loop1 
    global loop2
    global total_marks
    global passMarks
    global deferMarks
    global failMarks
    while loop1:
            total_marks = 0
            passMarks = validate_input("pass")
            total_marks = total_marks + int(passMarks)
            deferMarks = validate_input("defer")
            total_marks = total_marks + int(deferMarks)    
            failMarks = validate_input("fail")
            total_marks = total_marks + int(failMarks)
            if total_marks == 120:
                result = calculateRank()
                print(result)
                temp = [result,passMarks,deferMarks,failMarks,]
                list1.append(temp)

            #Loop for the program continuing   
                while loop2:
                     print("Would you like to enter another set of data?")
                     play_again=str(input("Enter 'Y' for yes or 'Q' to quit and view results:"))
                     play_again = play_again.upper()
                     if play_again == "Y":
                       break
                     if play_again == "Q":
                       loop1 = False
                       loop2 = False
                     else:
                       print("Invalid input")
            else:
                print("Incorrect Total")
                
#Loop for the getting user mode 
while loop3:
    print("To select the student mode enter - STU \nTo select the staff mode enter - STF")
    mode = input("Enter the mode you want to use-")
    if mode == "STU" or mode == "STF":
        break
    print("Invalid input")
    loop3 = True
        
#Loop for the getting user privileged data    
while loop4:
        if mode == "STU":
                main()
                break
        elif mode == "STF":
                main()
                print("""
    To print Horizontal Histogram enter - H
    To print Vertical histogram enter - V
    To print List enter - L
    To write data into to text file and print data enter - T
    To end program enter - E
            """)
                userChoice = input("Enter you choice:-")
                userChoice = userChoice.upper()
                if userChoice == "H":
                    Horizontal_histogram(Progress,Trailer,Exclude,Retriever)
                elif userChoice == "V":
                     Vertical_histogram(Progress,Trailer,Exclude,Retriever)
                elif userChoice == "L":
                    print(list1)
                elif userChoice == "T":
                    write_data(list1)
                elif userChoice == "E":
                    break
     
print("Thank you!")




        
