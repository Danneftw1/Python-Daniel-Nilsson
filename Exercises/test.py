import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import numpy as np

x = 0
y = 0

bredd = 6
hojd = 6

xbredd = (x - bredd/2)
xhojd = (y - hojd/2)

# (x1 + b/2 * y1 + h/2)

rect = Rectangle((xbredd, xhojd), bredd, hojd, alpha=0.3, fill=True, color="b") #förkortning funkar för färgen
circle = Circle((0,0), 5, alpha=0.3, fill=True, color="r")


plt.figure(figsize=(10, 10))
plt.axis([-10, 10, -10, 10])
plt.gca().add_patch(rect);
plt.gca().add_patch(circle);
plt.show() # funkar för .py-filer