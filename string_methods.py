'''
1. Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = "P@#yn26at^&i5ve"
Output: Chars = 8 Digits = 2 Symbol = 3
'''
def count_chars_digits_symbols(input_string):
    chars = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    symbols = len(input_string) - chars - digits
    print("Count all letters, digits, and special symbols from the given string:")
    print("Chars =" ,chars, "Digits =", digits, "Symbols =", symbols)

input_string1 = "P@#yn26at^&i5ve"
print("Main string",input_string1)
count_chars_digits_symbols(input_string1)
print("---------------------------------------------------")

'''
2. Write a Python program to remove duplicate characters of a given string.
Input = "String and String Function"
Output: String and Function
'''

def remove_duplicate_characters(input_string):
    result = ""
    seen = set()
    for char in input_string:
        if char not in seen:
            result += char
            seen.add(char)
    return result

input_string2 = "String and String Function"
print("Main string:",input_string2)
output2 = remove_duplicate_characters(input_string2)
print("After removing duplicate characters from string :",output2)
print("---------------------------------------------------")

'''3. Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11
'''

def count_upper_lower_special_numbers(input_string):
    uppercase = sum(c.isupper() for c in input_string)
    lowercase = sum(c.islower() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    special = len(input_string) - uppercase - lowercase - digits
    print("UpperCase:", uppercase)
    print("LowerCase:" ,lowercase)
    print("NumberCase:",digits)
    print("SpecialCase:" ,special)

input_string3 = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print("Count Uppercase, Lowercase, special character and numeric values in a given string :")
print("Main string",input_string3)
count_upper_lower_special_numbers(input_string3)
print("---------------------------------------------------")

'''
4. Write a Python Count vowels in a string
input= "Welcome to Python Assigment"
'''

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(c in vowels for c in input_string)
    print("Vowels:" ,count)

input_string4 = "Welcome to Python Assigment"
print("Count vowels in a string:")
print("Main string:",input_string4)
count_vowels(input_string4)

