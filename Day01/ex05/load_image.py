from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Takes the path of a file in parameter,
    prints his format and its pixel content in RGB format
    """
    try:
        image = Image.open(path)
    except IOError:
        print(f"Can't open {path}")
        exit(1)
    np_img = np.array(image)
    print(f"The shape of the image is : {np_img.shape}")
    return np_img
