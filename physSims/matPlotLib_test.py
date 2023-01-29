import matplotlib.pyplot as plt

data =  (1,5,2,3)
xVals = [1,2,3,4]
yVals = [3 for _ in range(4)]

fig, simple_chart = plt.subplots()

# simple_chart.plot(data)
simple_chart.plot(xVals,yVals, 'o', color='tab:brown')

plt.show()