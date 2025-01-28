

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def average(x, y):
    # Check if x and y is numbers
    if not is_number(x) or not is_number(y):
        raise Exception("Argument is not a number")

    return (x+y)/2    
        