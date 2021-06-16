#inputs
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hrs rate:")
r=float(rate)
#minimum number of hours
minh = 40
#condition
if h>40:
    extrah=h-40
    gp = extrah*1.5*r + 40*r
else:
    gp = h*r
#output
print (gp)
