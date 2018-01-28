import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Physical parameters
L = 1
w1 = 1
w2 = np.sqrt(3)*w1
d1 = 0.1
d2 = 0.3
def x1(t):
  return 0.5*(d1+d2)*np.cos(w1*t) + 0.5*(d1-d2)*np.cos(w2*t) + L/3
def x2(t):
  return 0.5*(d1+d2)*np.cos(w1*t) - 0.5*(d1-d2)*np.cos(w2*t) + 2*L/3

# Animation parameters
Nperiod = 3
animation_time = 5

# Parameter setup
wmin = w1
Tmax = 2*np.pi/wmin
t = np.linspace(0,Nperiod*Tmax,2000)
interval = 1000.*animation_time/len(t)
xmin = min(x1(t))
xmax = max(x2(t))

# Plot setup
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(t,x1(t), color='r')
ax1.plot(t,x2(t), color='b')
ax1.set_xlim(-0.1, 3.1*Tmax)
ax2.set_xlim(-0.2, L + 0.2)
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
pt1 = patches.Ellipse((x1(0),0), semit, semix, fc='r')
pt2 = patches.Ellipse((x2(0),0), semit, semix, fc='b')

bbox = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width, height = bbox.width, bbox.height
semix = 0.1*(xmax-xmin)
semiy = semix/(xmax-xmin)*0.5*width/height
m1 = plt.Rectangle((0,0), semix, semiy, fc='r')
m2 = plt.Rectangle((0,0), semix, semiy, fc='b')

def init():
  ax1.add_patch(pt1)
  ax1.add_patch(pt2)
  m1.center = (0,0)
  m2.center = (0,0)
  ax2.add_patch(m1)
  ax2.add_patch(m2)
  return m1, m2,

def animate(i):
  m1.xy = (x1(t[i]), m1.xy[1])
  m2.xy = (x2(t[i]), m2.xy[1])
  pt1.center = (t[i], x1(t[i]))
  pt2.center = (t[i], x2(t[i]))
  return m1, m2, pt1, pt2,

anim = animation.FuncAnimation( fig, animate,
                                init_func=init,
                                frames=len(t),
                                interval=interval,
                                blit=True)

plt.show()
