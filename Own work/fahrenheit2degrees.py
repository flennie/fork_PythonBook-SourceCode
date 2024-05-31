
import matplotlib.pyplot as plt
import numpy as np

min =0
max =213

#degF = 212

xaxis = [0]
yaxis =[0]


for degF in range(min, max):
    degC = 5 / 9 * (degF - 32)
    yaxis.append(degC)
    xaxis.append(degF)
    print(degF, " --> ", degC, " | ", max)

fig = plt.figure()
ax = plt.axes()
ax.plot(xaxis, yaxis)
plt.show()

degC =100
degF=(9/5*degC)+32
print(degC, 'graden Celcius is ', degF, ' graden Fahrenheid')



