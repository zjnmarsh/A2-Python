#triangle wave
import numpy as np
import matplotlib.pyplot as plt


numSines = int(input("enter numebr of sine waves you wish to add "))

t=np.arange(0,10,0.1)
y=np.zeros(100)
for i in range(numSines):
    # factor = 2* i+1 # square wave and
    factor = i+1
    y = y + np.sin(factor*t)/factor
    y = y + (((-1)**(factor-1)/2)/factor*factor)
#plotting instructions
fig, ax = plt.subplots()
ax.plot(t, y)

ax.set(xlabel='time (s)', ylabel='amplitude',
       title='Triangle wave is a sum of ' + str(numSines) + ' sine waves')
ax.grid()

fig.savefig("test.png")
plt.show()
