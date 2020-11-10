#takes 2 numbers as input. 
#If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. 
#Otherwise return false
def func(num1, num2):
    if((num1 == 3 or num2 == 3) and str(num1 + num2).find('3') != -1):
        return True
    else:
        return False
