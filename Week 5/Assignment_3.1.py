#Write a program to prompt the user for hours and rate per hour using input to
#compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
#hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
#10.50 per hour to test the program (the pay should be 498.75). You should use
#input to read a string and float() to convert the string to a number. Do not
#worry about error checking the input-assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
rph = input('Enter the rate per hour:')
new_rph=float(rph)
if h <=40 :
    gross_pay = h * new_rph
    print(gross_pay)
else :
    new_h=h-40
    gross_pay = (40 * new_rph) + (new_h *1.5 * new_rph)
    print(gross_pay)
