# use bin() to convert to its binary representation
# use count() to see how many times the character appears

def count_bits(n):
    return bin(n).count('1')
print(count_bits(1234))