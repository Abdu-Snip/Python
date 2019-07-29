while True:
	base=int(input("Enter the length of triangle's base: "))
	if(base>0):
		break
	else:
		print('Enter a positive number')	
while True:        
	height=int(input("Enter the length of triangle's height: "))
	if(height>0):
		break
	else:
		print('Enter a positive number')
while True:    
	hyp=int(input("Enter the length of triangle's third side: "))
	if(hyp>0):
		break
else: 
	print('Enter a positive number')
print('\nArea of triangle =',int(base*height),'\nPerimeter of triangle =',base+height+hyp)
