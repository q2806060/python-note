import matplotlib.pyplot as mp 

mp.figure("Locator", facecolor="lightgray")

ax = mp.gca()
ax.spines['left'].set_color("none")
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
mp.ylim(-1,1)
mp.xlim(0,10)
mp.yticks([])
ax.spines['bottom'].set_position(('data', 0))

l1 = mp.MultipleLocator(1)
ax.xaxis.set_major_locator(l1)

l2 = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(l2)
mp.show()