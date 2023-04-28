#CHAMATH DIKLSHAN MAHAPATUNA
#w1902042
#Importing functions from diffrent files
#function for  Vertical_histogram    
def Vertical_histogram(Progress,Trailer,Exclude,Retriever):
    print("\t\t\tVertical Histogram")
    print("Progress\tTrailer\t\tRetrieve\tExclude")
    for i in range(1,((max(Progress ,Trailer ,Exclude ,Retriever))+1)):
        print("\n")
        if i <= Progress:
            print("*", end =" ")
        else:
            print(end =" ")
        if i <= Trailer:
            print("\t\t*", end =" ")
        else:
            print("\t\t", end =" ")
        if i <= Retriever:
            print("\t\t*", end =" ")
        else:
            print("\t\t",end =" ")
        if i <= Exclude:
            print("\t\t* ", end=" ")
        else:
            print(end=" ")
        print()
    total=Progress +Trailer +Exclude+Retriever
    print(total,"outcomes in total")
        
