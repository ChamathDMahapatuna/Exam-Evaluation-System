#CHAMATH DIKLSHAN MAHAPATUNA
#w1902042
#Importing functions from diffrent files
#function for Horizontal histogram   
def Horizontal_histogram(Progress,Trailer,Exclude,Retriever):
    print("-----------------------------------------------------------")
    print("\t\t\tHorizontal Histogram")
    print("Progress:          ",Progress *" * ")
    print("Trailing :         ",Trailer *" * ")
    print("Exclude_students:  ",Exclude*" * ")
    print("retriever_students:",Retriever*" * ")
    total=Progress +Trailer +Exclude+Retriever
    print(total,"outcomes in total")
    print("-----------------------------------------------------------")

