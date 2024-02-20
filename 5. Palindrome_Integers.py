def is_palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False

def separate_elements(text, sep):
    numbers_as_string = text.split(sep)
    return numbers_as_string

data = input()
nums_string = separate_elements(data, ", ")

for el in nums_string:
    print(is_palindrome(el))
