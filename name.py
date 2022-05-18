#Name: Jose Melquiades Escobar

#Define main():
def main ():

    #Declare Local variables
    full_name = 0
    name_list = 0
    initial = 0
    name_initials = []

    #Prompt user to enter the full name
    full_name = input ('Enter your full name: ') 

    #Use split method to split the full name
    name_list = full_name.split()

    #User for loop to get first character of each name as an initial
    for name in name_list:
        initial = name[0]
        name_initials.append(initial)

    #Display output
    print (name_initials[0], '.', name_initials[1], '.', name_initials[2], '.', sep = '')



main () 
