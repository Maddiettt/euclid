# NOTE: a big project organizes itself to many modules, or libraries.
# to use a library, we first need to import it
# The sys has goodies about system, like command line arguemnts, exit
# we use random to generate a random number.
import sys
import random

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: guess range")
        # NOTE: exit will exit the program.  By convention, an exit
        # code of 0 indicate success.  exit of none zero value indicates
        # some kind of failure.
        sys.exit(1)
        
    # Exercise: What is sys.argv[0]?   Print it out.
    max = int(sys.argv[1])
    # Exercise: Google python random.randint, read the document.
    # Is it possible for randint(1, 10) to return 1?  10?
    secret = random.randint(1, max)
    cnt = 0
    
    while True:
        # cnt++, and cnt += 1 both mean cnt = cnt + 1
        cnt += 1
        print("Guess a number:")

        # input is a built in function that read input from command line.
        val = input()

        # convert val (which is a string right now) to int
        val = int(val)

        # Implement the following
        # if value equals secret, print a congratulation message and exit.
        # other wise, give user hint if the guess is too big or too small
        # but never reveal the secret to user.
