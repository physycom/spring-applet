import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Physical parameters
F0 = 1
m = 1
w0 = 1
w = 1.01
def x(t):
  return F0/m/(w0**2-w**2)*(np.cos(w*t)-np.cos(w0*t))

# Animation parameters
Nperiod = 3
animation_time = 30

# Parameter setup
wmin = min(abs(w-w0),w+w0)/2
Tmax = 2*np.pi/wmin
t = np.linspace(0,Nperiod*Tmax,2000)
interval = 1000.*animation_time/len(t)
xmin = min(x(t))
xmax = max(x(t))

# Plot setup
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(t,x(t), color='b')
ax1.set_xlim(-0.1, 3.1*Tmax)
ax2.set_xlim(1.2*xmin,1.4*xmax)
ax2.set_ylim(0,0.5)
ax2.spines['left'].set_color('none')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
plt.gca().axes.get_xaxis().set_ticks([])
plt.gca().axes.get_xaxis().set_ticklabels([])
plt.gca().axes.get_yaxis().set_ticks([])
plt.gca().axes.get_yaxis().set_ticklabels([])

bbox = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
semix = 0.07*(xmax-xmin)
semit = semix/(xmax-xmin)*(3*Tmax)/width*height
pt = patches.Ellipse((0,0), semit, semix, fc='b')

bbox = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
semix = 0.1*(xmax-xmin)
semiy = semix/(xmax-xmin)*0.5*width/height
m1 = plt.Rectangle((0,0), semix, semiy, fc='b')

def init():
  ax1.add_patch(pt)
  m1.center = (0,0)
  ax2.add_patch(m1)
  return m1,

def animate(i):
  m1.xy = (x(t[i]), m1.xy[1])
  pt.center = (t[i], x(t[i]))
  return m1, pt,

anim = animation.FuncAnimation( fig, animate,
                                init_func=init,
                                frames=len(t),
                                interval=interval,
                                blit=True)

plt.show()
