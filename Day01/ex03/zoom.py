from load_image import ft_load
import numpy as np
from PIL import Image


def zoom(path: str) -> None:
    """
    Takes a path of a file in parameter, print some information,
    slice it to (400, 400), transomrm it on B&W, and zoom on it
    Then, it display the new image
    """
    array = ft_load(path)
    print(array)
    data = Image.fromarray(array)
    imCrop = data.crop((450, 100, 850, 500))
    imCrop = imCrop.convert("L")
    np_img = np.asarray(imCrop)
    print(f"New shape after slicing: {np_img.shape}")
    print(np_img)
    imCrop.show()


def main():
    """
    Execute the zoom function with the filename
    """
    zoom("animal.jpeg")
    return 0


if __name__ == "__main__":
    main()
