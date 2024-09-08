from random import choice
import string

# Entry as a test
password = input('Enter your password: ')

# Data
numbers = list(string.digits)
low_letter = list(string.ascii_lowercase)
up_letter = list(string.ascii_uppercase)
symb = list(string.punctuation)
hex_digits = list(string.hexdigits)   
oct_digits = list(string.octdigits)  

# All in one combined list
comb = numbers + low_letter + up_letter + symb + hex_digits + oct_digits

crack = ''
attempts = 0

# Loop to generate guesses
while crack != password:
    crack = ''
    for _ in range(len(password)):
        crack += choice(comb) 
    attempts += 1
    print(f'Attempt {attempts}: {crack}')

print('Password cracked successfully!')
print(f'Your password is: {crack}')
