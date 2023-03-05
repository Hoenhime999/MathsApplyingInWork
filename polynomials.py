import numpy as np
import matplotlib.pyplot as plt



print("Please type the cofficients in the order x^n,x^n-1 up to x^0. Type done when cofficient of x^0 is typed")
colist = []


while True:
    co = input('Cofficient: ')
    try:
        colist.append(float(co))
    except ValueError:
        if co == 'done':
            break
        else:
            print('an error has occured ')
    

def y_value(x,coeff):
    
    coeff_deg = len(coeff)

    ys = np.zeros(len(x))
    for i in range(coeff_deg):
        ys += coeff[i] * x**i
    return ys

roots = np.roots(colist)
print(roots)
print(np.poly1d(colist))
colist.reverse()

x = np.linspace(-100,100)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y_value(x,colist))
plt.show()





