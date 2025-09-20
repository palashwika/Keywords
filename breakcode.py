#Take user input
a = input("Enter a word: ")
counter=0
#program to check break keyword
for i in a: #iterate for loop
    if (i=='A'): #condition 1, single quotes are used for single character A
    #display result
        print("A is found")
        break 
    else:
        #print("A not found")
        counter=1
if counter==1:
    print("A not found")
