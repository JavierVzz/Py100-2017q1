# Javier Vazquez
# Grid Printer
# Feb 17, 2017
# Description: http://uwpce-pythoncert.github.io/IntroPython2016a/exercises/comprehensions_lab.html
import os

def main():

    food_prefs = {"name":"Chris", "city":"Seattle", "cake":"chocolate", "fruit":"mango",
               "salad":"greek", "pasta":"lasagna"}

    print("\033[1m {0} is from {1}, and he likes {2} {3}, {4} {5}, \n \033[0m {6} {7}, and {8} {9}"
          .format(food_prefs["name"], food_prefs["city"], food_prefs["cake"], "cake",
                  food_prefs["fruit"], "fruit", food_prefs["salad"], "salad", food_prefs["pasta"],
                  "pasta"))

    dict_decHex = {}

if __name__ == '__main__':
    print(os.path.basename(__file__))
    print(main.__doc__)
    main()