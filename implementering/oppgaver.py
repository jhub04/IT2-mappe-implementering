import matplotlib.pyplot as plt

# Oppgave 3

def f(x):
    return 2*x-3

x = []
y = []

for i in range(5):
    x.append(i)
    y.append(f(i))

plt.xlabel("$x$")
plt.ylabel("$y$")

plt.style.use("bmh")
plt.plot(x, y)
plt.show()