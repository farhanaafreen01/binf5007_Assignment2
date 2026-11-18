import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column

    numbers = []
    count = 0

    with open(filepath, 'r') as infile:
        for line in infile:
            count = count + 1

            try: 
                value = line.rstrip('\n').split('\t')[column]
                
            except IndexError: 
                print("Exiting. The is no valid 'list index'  in column",column,  "in line " , count , "in file: " , filepath)
                sys.exit(1)

            try: 
                num = float(value)
            except ValueError:
                continue

            if math.isnan(num):
                continue
            

            numbers.append(num)

        if len(numbers) == 0:
            print("Error: There were no valid number(s) in column ", column, "in file: " , filepath)
            sys.exit(1)
            
    return numbers, count


def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    
    average = sum(numbers)/len(numbers)
    
    return float(average)  

    

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    min_num = min(numbers)
    max_num = max(numbers)

    return float(max_num) , float(min_num) 

    

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    
    n = len(numbers)

    if n <= 1:
        return 0.0

    mean = calculate_average(numbers)

    variance = 0 
    for num in numbers:
        variance = variance + (((num - mean) ** 2) / (n-1))

    return float(variance) 



def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    
    std_dev = math.sqrt(calculate_variance(numbers))

    return float(std_dev)


def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    
    sorted_num = sorted(number)

    n = len(sorted_num)

    middle_value = n // 2 

    if n % 2 == 1: 
        return float(sorted_num[middle_value])

    else: 
        return float((sorted_num[middle_value - 1] + sorted_num[middle_value] ) / 2 )



