import math

def polysum(n, s):
    """
    Input: n: number of sides, s: length of sides
    Output: sum = area + perimeter^2, rounded to 4 decimal places
    """
    #calculate area
    pi = math.pi
    area = (0.25*n*s**2)/math.tan(pi/n)
    
    #calculate perimeter
    perimeter = s*n
    
    #return the sum of area and perimeter^2 to 4 decimal places 
    sum = area + perimeter**2
    return format(sum, '.4f')