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
        print 'Note: To ensure that you get an accurate and meaningful answer when performing tetration, the second number needs to be a positive integer'
        print ''
        print 'Enter the second number (b), and then press enter.'
        print ''
        print 'The two numbers will be combined with the mathematical operation of your choice.'
        print 'Then the awnser will be displayed.'
        print ''
        print 'If you want to end the program after seeing the result, type "kill", and then press enter.'
        print 'If you want to make another calculation instead, type anything else or nothing at all, and then press enter.'
        print '--------------------------------------------.'
        enter=raw_input('Press enter to continue and make a normal calculation or enter "s" to activate the bonus feature for the next calculation.')
    else:
        try: cal.append(float(a))
        except ValueError:
            print 'That is not a number! Please try again...'
            continue
        cal.append(raw_input('Enter the operation you want to perform.'))
        if cal[1]!='+' and cal[1]!='-' and cal[1]!='x' and cal[1]!='/' and cal[1]!='^' and cal[1]!='r' and cal[1]!='^^':
            print 'That is not a valid operation! Please try again...'
            continue
        try: cal.append(float(raw_input('Enter the second number.')))
        except ValueError:
            print 'That is not a number! Please try again...'
            continue
        if cal[1]== '+': cal.append(cal[0]+cal[2])
        if cal[1]== '-': cal.append(cal[0]-cal[2]) 
        if cal[1]== 'x': cal.append(cal[0]*cal[2])
        if cal[1]== '/':
            try: cal.append(cal[0]/cal[2])
            except ZeroDivisionError: cal.append('Divide By Zero Error')
        if cal[1]== '^':
            try: cal.append(cal[0]**cal[2])
            except ZeroDivisionError: cal.append('Cannot Raise Zero to a Negative Exponent')
            except ValueError: cal.append('Cannot Take a Fractional Power of a Negative Number')
            except OverflowError: cal.append('Answer Too Big')
        if cal[1]== 'r':
            try: cal.append(cal[2]**(1/cal[0]))
            except ZeroDivisionError: cal.append('Cannot Take a Zeroth Root')
            except ValueError: cal.append('Cannot Take the Radical of a Negative Number')
            except OverflowError: cal.append('Answer Too Big')
        if cal[1]== '^^':
            i=cal[2]-1
            k=cal[0]
            while i>0:
                try: k=cal[0]**k
                except OverflowError: cal.append('Answer Too Big')
                except: cal.append('Error')
                i=i-1
            cal.append(k)
            r=cal[2]-int(cal[2])
            if cal[2]<=0 or r!=0: print "Warning: Because you didn't enter a positive integer for the second number when tetrating, the answer may be incorrect and/or meaningless."
        print cal[0],'',cal[1],'',cal[2],' = ',cal[3]
        enter=raw_input('Press enter to make another calculation.')
