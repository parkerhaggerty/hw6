                    # Import stuff...

from math import sin
from numpy import arange, array, pi
from pylab import plot, xlabel, ylabel, show


                    # Main Program...

g = 9.81        # meters/second
l = 0.09        # meters (length of arm)

a = 0.0         # start of interval
b = 10.0        # end of interval
N = 10000.0     # number of steps
h = (b-a)/N     # size of single step

tpoints = arange(a, b, h)
theta_points = []
omega_points = []
r = array([(-175.0*(pi/180.0)), 0.0], float)

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta, fomega], float)

for t in tpoints:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6

print(theta_points)
plot(tpoints, theta_points)
xlabel("time")
ylabel("theta_points (radians)")
show()
    