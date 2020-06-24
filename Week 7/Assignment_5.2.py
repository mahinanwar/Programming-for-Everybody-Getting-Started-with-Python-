#Write a program that repeatedly prompts a user for integer numbers until the
#user enters 'done'. Once 'done' is entered, print out the largest and smallest
#of the numbers. If the user enters anything other than a valid number catch it
#with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break

    try:
        new_num=int(num)
    except:
        print('Invalid input')
   # if num == "done" :
    #    break
    else:
        if largest and smallest is None:
            largest=new_num
            smallest=new_num
        else:
            if new_num>largest :
                largest=new_num
            elif new_num<smallest :
                samllest=new_num

print("Maximum is", largest)
print("Minimum is", smallest)
