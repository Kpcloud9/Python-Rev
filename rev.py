import random
print('Password Generator')
chars='1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number=int(input('No. of passwords:'))
length=int(input('Password Count:'))
print('\nPasswords:')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)