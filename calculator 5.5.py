enter='yes'
while enter!='kill':
    print ''
    if enter=='s': print 'Warning: The bonus feature is currently turned on for this calculation.'
    a=(raw_input('Enter the first number or enter the word help for info'))
    if a=='kill': break
    if a=='s':
        if enter=='s': print 'The bonus feature has already been activated for this calculation, so there is no need to do it again.'
        enter='s'
        continue
    if a=='help':
        print '--------------------------------------------'
        print 'Instuctions for how to use the calculator:'
        print ''
        print 'Enter the first number (a), and then press enter.'
        print ''
        print 'Enter the operation exactly as shown, and then press enter.'
        print 'The list of possible operations are as follows:'
        print 'To perform addition and output the result "a + b", type "+", "plus", or "a" as the operation'
        print 'To perform subtraction and output the result "a - b", type "-" or "minus" as the operation'
        print 'To perform multiplication and output the result "a x b", type "x", "*", or "times" as the operation'
        print 'To perform division and output the result "a / b", type "/" or "divided by" as the operation'
        print 'To perform exponentiation and output the result "a ^ b", type "^" or "p" as the operation'
        print 'To perform the ath root of b and output the result, type "r" or "rad" as the operation'
        print 'To perform tetration and output the result "a ^^ b", type "^^", "t", or "tetrated to" as the operation'
        print 'Note: To ensure that you get an accurate and meaningful answer when performing tetration, the second number needs to be a positive integer'
        print ''
        print 'Enter the second number (b), and then press enter.'
        print ''
        print 'The two numbers will be combined with the mathematical operation of your choice.'
        print 'Then the awnser will be displayed.'
        print ''
        print 'If you want to end the program after seeing the result, type "kill", and then press enter.'
        print 'If you want to make another calculation instead, then repeat this process from the beggining.'
        print ''
        print 'Bonus Feature: If you want to switch the 2 numbers, then type "s" instead of entering the first number.'
        print 'After that, you will enter everything as normal, except the calculator will automatically switch the order of the two numbers.'
        print 'Pressing "s" an additional time is unneccesary and may put you into a repeated loop.'
        print 'The bonus feature must be reactivated for each calculation that it is to be used for.'
        print '--------------------------------------------.'
    else:
        cal=[]
        r=[]
        try: cal.append(float(a))
        except ValueError:
            print 'That is not a number! Please try again...'
            continue
        cal.append(raw_input('Enter the operation you want to perform.'))
        if cal[1] not in ['+', '-', 'x', '/', '^', 'r', '^^', 'plus', 'a', 'minus', '*', 'times', 'divided by', 'p', 'rad', 't', 'tetrated to']:
            print 'That is not a valid operation! Please try again...'
            continue
        try: cal.append(float(raw_input('Enter the second number.')))
        except ValueError:
            print 'That is not a number! Please try again...'
            continue
        r.append(cal[0]-int(cal[0]))
        r.append('n')
        r.append(cal[2]-int(cal[2]))
        if enter=='s':
            m=cal[0]
            d=cal[2]
            cal[0]=d
            cal[2]=m
        if cal[1]== '+' or cal[1]== 'plus' or cal[1]== 'a':
            cal.append(cal[0]+cal[2])
            cal.append('+')
            cal.append(' plus ')
        if cal[1]== '-' or cal[1]== 'minus':
            cal.append(cal[0]-cal[2])
            cal.append('-')
            cal.append(' minus ')
        if cal[1]== 'x' or cal[1]== '*' or cal[1]== 'times':
            cal.append(cal[0]*cal[2])
            cal.append('x')
            cal.append(' times ')
        if cal[1]== '/' or cal[1]== 'divided by':
            try: cal.append(cal[0]/cal[2])
            except ZeroDivisionError: cal.append('"Divide By Zero Error"')
            cal.append('/')
            cal.append(' divided by ')
        if cal[1]== '^' or cal[1]== 'p':
            try: cal.append(cal[0]**cal[2])
            except ZeroDivisionError: cal.append('"Cannot Raise Zero to a Negative Exponent"')
            except ValueError: cal.append('"Cannot Take a Fractional Power of a Negative Number"')
            except OverflowError: cal.append('"Answer Too Big"')
            cal.append('^')
            cal.append(' taken to the power of ')
        if cal[1]== 'r' or cal[1]== 'rad':
            try: cal.append(cal[2]**(1/cal[0]))
            except ZeroDivisionError: cal.append('"Cannot Take a Zeroth Root"')
            except ValueError: cal.append('"Cannot Take the Radical of a Negative Number"')
            except OverflowError: cal.append('"Answer Too Big"')
            cal.append('r')
        if cal[1]== '^^' or cal[1]== 't' or cal[1]== 'tetrated to':
            i=cal[2]-1
            k=cal[0]
            enter=True
            while i>0:
                try: k=cal[0]**k
                except OverflowError:
                    cal.append('"Answer Too Big"')
                    enter=False
                    break
                except:
                    cal.append('"Miscellaneous Tetration Error"')
                    enter=False
                    break
                i=i-1
            if enter==True: cal.append(k)
            if cal[2]<=0 or r[2]!=0: print "Warning: Because you didn't enter a positive integer for the second number when tetrating, the answer may be incorrect and/or meaningless."
            cal.append('^^')
            cal.append(' tetrated to ')
        try: r.append(cal[3]-int(cal[3]))
        except ValueError: r.append('error')
        if r[0]==0:
            w=str(cal[0])
            cal[0]=w[:-2]
        if r[2]==0:
            w=str(cal[2])
            cal[2]=w[:-2]
        if r[3]==0:
            w=str(cal[3])
            r[1]=w.count('e')
            if r[1]==0: cal[3]=w[:-2]
        enter='yes'
        print cal[0],'',cal[4],'',cal[2],' = ',cal[3]
        if cal[4]=='r': print 'The ',cal[0],'th root of ',cal[2],' is equal to ',cal[3]
        else: print cal[0],cal[5],cal[2],' is equal to ',cal[3]
