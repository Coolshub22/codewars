# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

# iterate through each character in the string
# check if its a letter
# convert to its position in the alphabet
# collect and return the positions as a space_Separated string

def alpha_pos(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            position = ord(char) - ord('a') + 1  # is a way to convert a letter into its position in the English alphabet
            result.append(str(position))
            
    return ' '.join(result)

print(alpha_pos("The sunset sets at 6 0'clock."))
