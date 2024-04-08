import say_hello
def main():
    name= input("Enter a name: ")
    say_hello.greeting(name)

    fav= input("What's your favorite?")
    say_hello.favorite(fav)

# set the enviornment for this script
# is it main, or is this a module being called by another script
if __name__== '__main__':
    main()