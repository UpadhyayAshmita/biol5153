def get_input():
    #multiplication table
    #ask for the size of multiplication matrix
    size= int(input("Enter the size of your table: "))
    cell_width= len(str((size * size))) + 1
    return (size, cell_width)

def print_table(n):
    #nested for loop
    for i in range(1,n+1):
        for j in range(1, n+1):
            print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end='')
        #print new line 
    print()

def main():
    input_num, width= get_input()
    print(input_num,width)
    #print_table(input_num)
# set the enviornment for this script
# is it main, or is this a module being called by another script
if __name__== '__main__':
    main()