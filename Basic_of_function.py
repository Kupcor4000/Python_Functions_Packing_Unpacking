#Basic assumption
num = 10

#Random basic functions examples
def print_favourite_movie(movie_title):
    print(movie_title)

def print_name():
    print("Name")

def set_num():
    num = 5 #Creating new variable num inside this functions
    char = 'a'
    
    
#main function    
print_favourite_movie("Title")  #calling function

#How functions operate on global variable
print("Num before set_num(): {}".format(num))
set_num()
#in function set_num() variable named num exist only in this function, function do not have acces to global variable
print("Num after set_num(): {}".format(num))
