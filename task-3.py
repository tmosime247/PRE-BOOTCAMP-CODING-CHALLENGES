#takes 2 numbers as input. 
#If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. 
#Otherwise return false.
def func(num1, num2):
    if((num1 == 65 or num2 == 65) or (num1 + num2) == 65):
        return True
    else:
        return False

