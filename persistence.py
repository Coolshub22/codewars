def persistence(num):
    count = 0
    
    while num >= 10:
        product =1 
        for digit in str(num):
            product *= int(digit)
        num = product
        count += 1
    return count


print(persistence(39))   # Output: 3
print(persistence(999))  # Output: 4
print(persistence(4))    # Output: 0
