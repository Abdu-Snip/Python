num1=input('Enter a number: ')
print('a = ',num1)
num2=input('Enter another number: ')
print('b = ',num2)
print('\nSwapping: \nWithout a third variable:')
num1=int(num1)+int(num2)#both
num2=int(num1)-int(num2)#num1
num1=int(num1)-int(num2)#num2
print('a = ',num1,'\nb = ',num2)
print('Using a third variable:')
hold=num1
num1=num2
num2=hold
print('a = ',num1,'\nb = ',num2)