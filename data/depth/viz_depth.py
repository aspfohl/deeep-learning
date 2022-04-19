
from matplotlib import pyplot as plt
import numpy as np

F = "BJ721E05W-J11@9=person_whole_front_depth"

data = np.load(f"data/depth/{F}.npy")
plt.imshow(data)
plt.colorbar()
fig = plt.gcf()
HEIGHT, WIDTH = 512, 320
fig.set_size_inches(WIDTH/50, HEIGHT/50)
plt.savefig(f"data/depth/demo-{F}.png")
