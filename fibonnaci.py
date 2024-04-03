#get the input
number = input("Enter the number: ")
#initialize the variable for calculating fibonacci number at this position in seq
a,b = 0,1 

#one way to calculate the fibonacci number
for i in range(int(number)):
    a,b = b, a+b
#store the result so its obvious
fibonacci_number = a
print('The fibonacci number for', number, 'is:', fibonacci_number)

#making three functions for getting input, calculating fibonacci and printing:

def get_input(input_number):
    return input_number

def calc_fibonacci(number):
    a,b= 0,1
    for i in range(number):
        a,b= b,a+b
    return a

def print_fib(number, fibonacci_number):
    print(f'The fibonacci number for, {number} is: {fibonacci_number}')

#calling function
input_number= get_input(9)
fibonacci_number= calc_fibonacci(input_number)
print_fib(input_number,fibonacci_number)
