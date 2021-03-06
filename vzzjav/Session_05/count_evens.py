# Javier Vazquez
# Count evens
# Feb 14, 2017
# Description: http://uwpce-pythoncert.github.io/IntroToPython/exercises/comprehensions_lab.html

import random, os

def count_evens(listNumbers):
    '''Count how many even number are in a list of numbers'''
    return len([number for number in listNumbers if number % 2 == 0])

def main():
    '''Pass n random integer numbers to count_evens() function'''
    n = 0
    while True:
        try:
            n = int(input("Length of list of numbers: "))
            break
        except ValueError:
            print("Incorrect input, please provide a positive integer number")

    print(count_evens([random.randint(1,9) for i in range(n)]))

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()