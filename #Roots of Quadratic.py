#Roots of Quadratic
def coefficients():
    a = int(input("Choose a coeffecient: "))
    b = int(input("Choose a coeffecient: "))
    c = int(input("Choose a coeffecient: "))
    return [a,b,c]
abc = coefficients()
print("Coefficients are:", abc)
a, b, c = abc
if b**2 - 4*a*c < 0:
    print("There are no real roots")
    k = b**2 - 4*a*c
    k = -k 
    z_r = -b/(2*a)
    z_i = (k**0.5) / (2*a)
    z_i2 = -(k**0.5) / (2*a)
    print('The first root:(' + str(z_r) + ',' + str(z_i) + 'i)')
    print('The second root:(' + str(z_r) + ',' + str(z_i2) + 'i)')

elif a == 0:
    print("This is not a quadratic")
else:
    x_1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)        
    print([x_1,x_2])
                 