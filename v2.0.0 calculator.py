print 'Type addition or add to add 2 numbers'
oper=raw_input("Type anything else to multiply 2 numbers.")
if oper=='addition' or 'add': # This is the addition calculator
    print 'The two numbwers you will type will be added'
    a=float(raw_input('Type the first number'))
    b=float(raw_input('Type the second number'))
    c=a+b
else: # This is the multipliation calculator
    print 'The two numbwers you will type will be multiplied'
    a=float(raw_input('Type the first number'))
    b=float(raw_input('Type the second number'))
    c=a*b
print "The awnser is",c
    

