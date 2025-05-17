def solution(text, ending):
    return text.endswith(ending)
print(solution("abcd", "cd")) # Returns True because 'abcd' ends with 'cd'
print(solution("abcd", "ef"))

# string.endswith(ending)
# This is a built-in Python method that returns True if string ends with the substring ending.

