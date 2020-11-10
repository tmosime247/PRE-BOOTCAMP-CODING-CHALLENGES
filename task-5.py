#takes in three numbers.
#These numbers represent the lengths of the sides of a triangle.
#The function should return the area of a triangle
import math

def area_of_triangle(len1, len2, len3):
        semi_perimeter = (1/2) * (len1 + len2 + len3)
        formula_data = (semi_perimeter - len1) * (semi_perimeter - len2) * (semi_perimeter - len3)
        area = math.sqrt(semi_perimeter * formula_data)
        return area
