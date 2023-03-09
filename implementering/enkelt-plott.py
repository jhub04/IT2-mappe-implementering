import matplotlib.pyplot as plt

x = []
y = []

def f(x):
    return 3*x+2

for i in range(5):
    x.append(i)
    y.append(f(i))


plt.plot(x, y) # Oppretter plott
plt.show() # viser plottet