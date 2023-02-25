EDL = 'a = bq + r'
#formula
HCF_not_found = True

try:
    num1 = int(input('Your first Number(positive): '))
    num2 = int(input('Your Second Number(positive): '))
    if num1 > num2:
        a = num1
        b = num2
    else:
        b = num1
        a = num2
    print(f'{a} = {b}* {a//b} + {a%b}')
    while HCF_not_found:
        
        if a%b != 0:
            r = a%b
            a = b
            b = r
            4052
            print(f'{a} = {b}* {a//b} + {a%b}')

        if a%b == 0:
            hcf = b
            print(f'Your hcf of numbers {num1} and {num2} is {hcf}')
            HCF_not_found = False

except:
    print('error has occurded please rerun the software')



