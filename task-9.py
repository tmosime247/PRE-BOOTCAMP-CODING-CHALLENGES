#sum of all the multiples of 3 or 5 below 1000
sum_ = 0
for num in range(1000):
    if((num != 0) and (((num % 3) == 0) or ((num % 5) == 0))):
        sum_ += num
    
print(sum_)
