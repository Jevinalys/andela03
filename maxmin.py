min = None
max = None
while True:
    inp = raw_input("Enter a number:")
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
         print 'invalid input'
         continue

    if min is None or num < min:
          min = num
          
    if max is None or num > max:
          max = num


print 'Maximum number ',int(max)
print 'Minimum number ',int(min)
