#check for odd number
num=int(input('Enter a number:'))
if num%2 != 0:
    print(f'The number {num} is odd number')

#check for even number
num=int(input('Enter a number:'))
if num%2 == 0:
    print(f'The number {num} is even number')

#check for string is palindrome
strr=input('enetr a string: ')
if strr==strr[::-1]:
    print(f'{strr} is palindrome')

#check greater number a=23 ,b=50
num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
if num2 > num1:
    print(f'The number {num2} is greater than {num1}')

#check string length is even
strr=input('Enter the string: ')
len(strr)
if len(strr)%2 == 0:
    print(f'the length of String {strr} is even ')

#check from list 
prog_list=eval(input('enter the programiing language list: '))
prog=input('enter the any languages want to check :')
if prog in prog_list:
    print("It's present")
if prog not in prog_list:
    print('Not present')

#check for postive number
num=int(input('Enter a number: '))
if num>=0:
    print(f'The number {num} is positive')

#check 1st character of string is consonant
strr=input('enter a string: ')
strr[0:1]
if strr[0:1]not in 'aeiou':
    print(f'{strr[0:1] } is consonant')

#check last letter is vowel
strr=input('enter a string: ')
strr[-1]
if strr[-1] in 'aeiou':
    print(f'{strr[-1] } is vowel')


#check for take chr and convert it into lower case if uppercase and convert it upper if in lower case
char = input("Enter a character: ")
if 'A' <= char <= 'Z':
    char = chr(ord(char) + 32)
if 'a' <= char <= 'z':
    char = chr(ord(char) - 32)
print("Converted character:", char)



#TO check given string is upper case
strr=input('Enter the string : ')
if strr.isupper() :
    print(f'The string {strr} is in a upper case')
if strr.islower():
    print(f'The string {strr} is not in a lower case')


#check to Print python is easy if num is greater than 1 and less than 5
num=int(input('Enter the number:'))
if num>1 and num<5:
    print('Python is easy')


#check num divided by 2 and 5 then convert it to complex
num=int(input('Enter the number:'))
if num%2==0 and num%5==0:
    print(f'The number {num} is convert into {complex(num)}')

