import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO # bytes io used for buffer memory to store on capture images

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

elephant_url = "https://thumbs.dreamstime.com/b/elephant-25928218.jpg"
elephant = load_image_from_url(elephant_url)

# display an original image
plt.figure(figsize = (6,4))
plt.imshow(elephant)
plt.title("Elephant")
plt.axis("off")
plt.show()

# Image to array
elephant_np = np.array(elephant)
print("elephant image shape",elephant_np.shape)

# gray scale image
elephant_gray = elephant.convert("L")
plt.figure(figsize = (6,6))
plt.imshow(elephant_gray,cmap = "vanimo")
plt.title("Elephant(grayscale)")
plt.axis("off")
plt.show()