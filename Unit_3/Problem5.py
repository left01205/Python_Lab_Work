import numpy as np
from PIL import Image


image = Image.open("C:\\Users\\admin\\Desktop\\test.jpg")

#  image to a NumPy array
image_array = np.array(image)

# Perform crop operation
cropped_image = image_array[100:300, 200:400]

# Perform flip operation
flipped_image = np.flip(cropped_image, axis=1)


flipped_pil_image = Image.fromarray(flipped_image)


flipped_pil_image.save("C:\\Users\\admin\\Desktop\\result.jpg")