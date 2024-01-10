enter='yes'
while enter!='kill':
    cal=[]
    a=(raw_input('Enter the first number or enter the word help for info'))
    if a=='help':
        print '--------------------------------------------'
        print 'Instuctions for how to use the calculator:'
        print ''
        print 'Enter the first number (a), and then press enter.'
        print ''
        print 'Enter the operation exactly as shown, and then press enter.'
        print 'The list of possible operations are as follows:'
        print 'To perform addition and output the result "a + b", type "+" as the operation'
        print 'To perform subtraction and output the result "a - b", type "-" as the operation'
        print 'To perform multiplication and output the result "a x b", type "x" as the operation'
        print 'To perform division and output the result "a / b", type "/" as the operation'
        print 'To perform exponentiation and output the result "a ^ b", type "^" as the operation'
        print 'To perform the ath root of b and output the result, type "r" as the operation'
        print 'To perform tetration and output the result "a ^^ b", type "^^" as the operation'
        print 'Note: To get an accurate and meaningful answer when performing tetration, the second number needs to be positive'
        print ''
        print 'Enter the second number (b), and then press enter.'
        print ''
        print 'The two numbers will be combined with the mathematical operation of your choice.'
        print 'Then the awnser will be displayed.'
        print ''
        print 'If you want to end the program after seeing the result, type "kill", and then press enter.'
        print 'If you want to make another calculation instead, type anything else or nothing at all, and then press enter.'
        print '--------------------------------------------.'
        enter=raw_input('Press enter to continue.')
    else:
        cal.append(float(a))
        cal.append(raw_input('Enter the operation you want to perform.'))
        cal.append(float(raw_input('Enter the second number.')))
        if cal[1]== '+': cal.append(cal[0]+cal[2])
        if cal[1]== '-': cal.append(cal[0]-cal[2]) 
        if cal[1]== 'x': cal.append(cal[0]*cal[2])
        if cal[1]== '/': cal.append(cal[0]/cal[2])
        if cal[1]== '^': cal.append(cal[0]**cal[2])
        if cal[1]== 'r': cal.append(cal[2]**(1/cal[0]))
        if cal[1]== '^^':
            i=cal[2]-1
            k=cal[0]
            while i>0:
                k=cal[0]**k
                i=i-1
            cal.append(k)
        print cal[0],'',cal[1],'',cal[2],' = ',cal[3]
        enter=raw_input('Press enter to make another calculation.')
