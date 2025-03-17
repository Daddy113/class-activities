# print("hello")
# n1=input("enter any text you want:")
# print(len(n1))




# n1=input("enter any text you want:")
# count=len(n1)
# for i in n1:
#     if i==" ":
#       count=count-1
# print(count)

# get=[]
# for i in range(1,6):
#     n1=input("enter the word:\n")
#     get.append(n1)
# for n1 in get:
#     print(len(n1.replace(" ","")))


# K: A
# J : I
# P: O
# T: E
# F: U

"""kajipotefu wkak"""
n1=input("enter the text\n")
n1=n1.upper()
n1 = list(n1)
for i in range(len(n1)):
    if n1[i] == "A":  # Second replacement (after 'k' has been replaced)
        n1[i] = "K"
    elif n1[i] == "K":  # First replacement
        n1[i] = "A"    
    elif n1[i] == "J":
        n1[i] = "I"
    elif n1[i] == "I":
        n1[i] = "J"
    elif n1[i] == "P":
        n1[i] = "O"
    elif n1[i] == "O":
        n1[i] = "P"
    elif n1[i] == "T":
        n1[i] = "E"
    elif n1[i] == "E":
        n1[i] = "T"
    elif n1[i] == "F":
        n1[i] = "U"
    elif n1[i] == "U":
        n1[i] = "F"
print(''.join(n1))      

       
        
        


