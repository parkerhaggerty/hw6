##  ##  This program uses the leap frog method  ##  ##                    
                    
                    # Import stuff...

from math import sin
from numpy import empty, arange, array, pi
from pylab import plot, xlabel, ylabel, show


                    # Main Program...


g = 9.81        # meters/second
l = 0.09        # meters (length of arm)

theta0 = 93.0*(pi/180.0)

a = 0.0         # start of interval
b = 10.0        # end of interval
N = 1000        # number of steps
H = (b-a)/N     # size of single step
delta= 10**(-8) #permitted error size

tpoints = arange(a, b, H)
theta_points = []
omega_points = []
r = array([theta0, 0.0], float) #convert to radians

def f(r):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta, fomega], float)

# Modified Midpoint...
for t in tpoints:
    theta_points.append(r[0])
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)
    R1=empty([1,2], float)
    R1[0]= 0.5*(r1+r2+0.5*H*f(r2))
    error=2*H*delta
    while error > H*delta:
        n += 1
        h = H/n
        # Modified Midpoint Method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)
        R2 = R1
        R1 = empty([n, 2], float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon 
        error = abs(epsilon[0])
    r = R1[n-1]

plot(tpoints, theta_points)
#plot(tpoints, theta_points, label='b.')
xlabel("t")
ylabel("theta")
show()
    