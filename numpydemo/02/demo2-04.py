import matplotlib.pyplot as mp

mp.figure("Flow layout", facecolor="lightgray")

mp.axes([0.1,0.1,0.8,0.3])
mp.text(0.5,0.5, '1',ha='center',va='center',size=36)

mp.axes([0.1,0.5,0.8,0.3])
mp.text(0.5,0.5, '2',ha='center',va='center',size=36)
mp.show()