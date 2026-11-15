import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column

    numbers = []
    count = 0

    with open (filepath, 'r') as infile:
        for line in infile:
            try: 
                value = line.rstrip('\n').split('\t')
            except IndexError: 
                print("Exiting. The is no valid index in column", {columm} ,  "in line " ,{count+1} , "in file" , {filepath})
                sys.exit(1)

            count = count + 1 

            try: 
                num = float(value)
            except: ValueError
                
            continue
        




    pass

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    pass

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    pass

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    pass

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    pass

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    pass


