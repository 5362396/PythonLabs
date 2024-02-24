true = 1
false = 0

print('Example no. 1 - operator |\n')
if true | false:
    print('true or false = true, prints')

if true | true:
    print('true or true = true, prints')

if false | false:
    print('false or false = false, does not print')

print('\nExample no. 2 - operator &\n')
if true & false:
    print('true and false = false, does not print')

if true & true:
    print('true or true = true, prints')

if false & false:
    print('false or false = false, does not print')

print('\nExample no. 3 - operator <<\n')
five = 5
print(five)  # 00101 = 5
print(five << 2)  # 10100 = 20

print('\nExample no. 4 - operator >>\n')
twelve = 12
print(twelve)  # 1100 = 12
print(twelve >> 2)  # 0011 = 3
