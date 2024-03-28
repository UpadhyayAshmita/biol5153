
#multiplication table
n=20
for i in range(1,n+1):
    for j in range(1, n+1):
        print(("{:6d}".format(i * j)), end='')
    print()