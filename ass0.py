from PIL import Image, ImageDraw

import numpy as np

import matplotlib.pyplot as plt


data = np.zeros( (150, 150), dtype = np.uint8)
fig = plt.figure( figsize = (8,8))

rows = 16;
columns = 16;

for i in range (1,rows*columns+1):
	for j in range(50,100):
		for k in range (50,100):
			data[j][k] = i;

	fig.add_subplot(rows, columns, i)
	plt.imshow(data)

plt.show()



# img = Image.fromarray(data)
# img.show()

