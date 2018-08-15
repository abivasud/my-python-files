num='' # The numerator of the fraction.
den='' # The denominator of the fraction.
output=1 # The result.
slash=1 # This is the location of the slash in the input.
location=0 # This is the current location in the input.
length=1 # The length of the input.
frac=raw_input('Enter the fraction.') # This is the input.
while True:
    if frac[slash]=='/': # Is the variable slash correct?
        break
    else:
        slash=slash+1
length= len(frac)
while True: # This section calculates the numerator.
    if location==slash: # Is the location at the slash?
        location=location+1 # Moves the location to the denominator.
        break
    else: # Then add it to the numerator.
        num=num,frac[location]
        location=loacation+1 # Move the location one step.
while True: # This section calculates the denominator.
    if location==length: # Is the location off the charts?
        break
    else: # Then add it to the denominator
        den=den,frac[location]
        location=location+1

        
    
        
