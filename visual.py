from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def print_img(response):
    img = mpimg.imread(BytesIO(response.content), format = 'JPG')
    plt.imshow(img)
    plt.show()