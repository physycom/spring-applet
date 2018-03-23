import numpy as np
import matplotlib.pyplot as plt

"""
Script which displays the solution to the linearized inverted pendulum,
i.e. a hyperbolic oscillator forced by a time-dependent square potential
"""

# Physical parameters
v0 = 1
f = 12
ti = 0.5*np.log((f+v0)/(f-v0))
tau = np.array([2*ti])
Tmax = 7*tau

def x(t, tau):
	ti = t - int(t/(2*tau))*2*tau
	if ti < tau:
		return v0*np.sinh(ti) + f*(1-np.cosh(ti))
	else:
		return v0*np.sinh(ti) + 2*f*(np.cosh(ti-tau)) - f*np.cosh(ti) - f

def v(t, tau):
	ti = t - int(t/(2*tau))*2*tau
	if ti < tau:
		return v0*np.cosh(ti) - f*np.sinh(ti)
	else:
		return v0*np.cosh(ti) + 2*f*np.sinh(ti-tau) - f*np.sinh(ti)

def E(t, tau):
	ti = t - int(t/(2*tau))*2*tau
	E = 0.5*v(ti,tau)**2 - 0.5*x(ti,tau)**2
	if ti < tau:
		return E + f*x(ti,tau)
	else:
		return E - f*x(ti,tau)

# Parameter setup
t = np.linspace(0,Tmax,2000)
xt = [np.array(list(map(lambda ti : x(ti,taui), t))) for taui in tau]
vt = [np.array(list(map(lambda ti : v(ti,taui), t))) for taui in tau]
Et = [np.array(list(map(lambda ti : E(ti,taui), t))) for taui in tau]

# Plot setup
fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=plt.figaspect(0.4))
ax1.set_xlabel("x(t)"); [ax1.plot(t,x) for x in xt]
ax2.set_xlabel("v(t)"); [ax2.plot(t,v) for v in vt]
ax3.set_xlabel("E(t)"); [ax3.plot(t,E) for E in Et]; ax3.set_ylim([0, 1])
[ax.axvline(i*taui, color='r') for i in np.arange(0,Tmax/tau) for taui in tau for ax in [ax1, ax2, ax3]]
plt.show()
