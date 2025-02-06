def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32


def count_words(sentence):
    if isinstance(sentence, str):
        return len(sentence.split())
    else:
        return None


def find_median(numbers):
    # Check if numbers is a list
    if not isinstance(numbers, list):
        return None
    
    # Check if list is not empty
    numbers_length = len(numbers)
    if not numbers_length > 0:
        return None

    # Check if numbers is made of 
    for element in numbers:
        if not isinstance(element,(int,float)):
            return None
    
    # Sort list
    numbers.sort()

    # Odd number of elements 
    if numbers_length % 2 == 1:
        index = int((numbers_length-1)/2)
        return numbers[index]

    # Even number of elements
    else:
        index1 = int(numbers_length/2-1)
        index2 = int(numbers_length/2)
        return (numbers[index1] + numbers[index2])/2
    

def is_sorted_ascending(numbers):
    return None