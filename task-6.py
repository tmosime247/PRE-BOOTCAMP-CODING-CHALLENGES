#takes in three numbers  
#returns the maximum number.
def max_num(num1, num2, num3):
    num_list = [num1, num2, num3]
    max_nm = 0
    for num in num_list:
        if(num > max_nm):
            max_nm = num
    return max_nm
