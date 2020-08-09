#* - information that we intend to pack every information to one variable
#Packing
def packer(*args):
    print(args)
    for i in range(len(args)):
        print(args[i])
        
    
#function which add unknown amount of prices of items
def calculate_total(*args):
    total = 0
    for i in range(len(args)):
          total += args[i]
    return total
 
#Unpacking    
def unpacker():
    return(1,2,30)

def separate_info(name):
    list = name.split(" ")
    return list


           
#main program
packer("Hello","my","name","is","John","Cena")
total = calculate_total(12,32,55,33,21,4,23,64,12,44,32,1,1,1)
print("\n{}\n".format(total))
v1,v2,v3 = unpacker()
print(unpacker())
print(v1)
print(v2)
print(v3)

full_name = input("Please enter your full name: \n")
user_name, user_surname = separate_info(full_name)
print(user_name)
print(user_surname)