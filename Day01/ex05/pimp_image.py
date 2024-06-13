import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    array[:, :, 0] = 255 - array[:, :, 0]
    array[:, :, 1] = 255 - array[:, :, 1]
    array[:, :, 2] = 255 - array[:, :, 2]
    Image.fromarray(array).show()
    return array


def ft_red(array) -> np.ndarray:
    """
    Apply a red filter to the image received.
    """
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    Image.fromarray(array).show()
    return array


def ft_green(array) -> np.ndarray:
    """
    Apply a green filter to the image received.
    """
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    Image.fromarray(array).show()
    return array


def ft_blue(array) -> np.ndarray:
    """
    Apply a blue filter to the image received.
    """
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    Image.fromarray(array).show()
    return array


def ft_grey(array) -> np.ndarray:
    """
    Apply a grey filter to the image received.
    """
    grey = np.mean(array[:, :, :3], axis=2)
    Image.fromarray(grey).show()
    return array
