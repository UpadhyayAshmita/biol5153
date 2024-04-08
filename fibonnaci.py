import argparse

def get_args():
    #create an argumentparser object
    parser= argparse.ArgumentParser(description='This script returns the fibonacci number at a \
                                     specified loc in fibonacci sequence')
    #making three functions for getting input, calculating fibonacci and printing:
    #add positional arguments(these are the ones that are absoultely essential/required)
    parser.add_argument("num", help= "the fibonacci number you wish to calculate", type=int)
    #add optional arguments
    #if 'store_true', this means assign 'True' if the argument is specified on the command
    #line, so the default for 'store_true' is false
    parser.add_argument("-v", "--verbose", help="Print verbose output or not", action='store_true')
    #parse the actual arguments
    args= parser.parse_args()
    return args

def calc_fibonacci(beyonce):
    a,b= 0,1
    for i in range(int(beyonce)):
        a,b= b,a+b
        fibonacci_number= a
    return fibonacci_number

def print_fib(number, fibonacci_number):
     
    if args.verbose:
        print('The Fibonacci number for', number, 'is:', fibonacci_number)
    else:
        print(fibonacci_number)

def main():
    #calculte fibonacci number
    fibonacci_number= calc_fibonacci(args.num)
    #print the fibonacci number
    print_fib(args.num,fibonacci_number)

#get the command line arguments
args= get_args()

# set the enviornment for this script
# is it main, or is this a module being called by another script
if __name__== '__main__':
    main()
