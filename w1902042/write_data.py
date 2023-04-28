#CHAMATH DIKLSHAN MAHAPATUNA
#w1902042
#Importing functions from diffrent files
#function for progression data to a list & to a text file
def write_data(list1):
    print("-----------------------------------------------------------")
    print("\t\t\tPrinting the items of the list")
    f = open("myfile.txt", "w")
    for i in range(len(list1)) :
          print(list1[i][0]," - ",list1[i][1],",",list1[i][2],",",list1[i][3])
          f.write(str(list1[i][0])+" - "+str(list1[i][1])+","+str(list1[i][2])+","+str(list1[i][3]))
          print(end=" ")
          f.write("\n")
          print()
    print("-----------------------------------------------------------")
    
    f.close()
    print("-----------------------------------------------------------")
    print("\t\t\topen and read the file ")
    #open and read the file after the appending:
    f = open("myfile.txt", "r")
    print(f.read())
    print("-----------------------------------------------------------")
