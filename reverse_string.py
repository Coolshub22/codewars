def solution(string):
    r_string = string[::-1]
    return r_string
print(solution("cools"))

# to reverse a string we use reverse() or [::-1]


# REVERSE EXAMPLE 2:
def spin_words(sentence):
# break the sentence into a list of words using split()
    words = sentence.split()     
# list comprehension
# reverse then join
    r_sentence = [word[::-1] if len(word) >= 5 else word
                  for word in words]
    return ' '.join(r_sentence)
print(spin_words("I We think about ourselves always"))