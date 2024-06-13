from load_image import ft_load
import numpy as np
from PIL import Image


def rotate(path: str) -> None:
    """
    Takes a path of a file in parameter, print some information,
    slice it to (400, 400), transomrm it on B&W, and transpose it
    Then, it display the new image
    """
    array = ft_load(path)
    print(array)
    imageList = array.tolist()
    transposed = [[imageList[j][i] for j in range(len(imageList))]
                  for i in range(len(imageList[0]))]
    array = np.array(transposed).astype(np.uint8)
    data = Image.fromarray(array)
    imCrop = data.crop((100, 450, 500, 850)).convert("L")
    np_img = np.asarray(imCrop)
    print(f"New shape after Transpose: {np_img.shape}")
    print(np_img)
    imCrop.show()


def main():
    """
    Execute the rotate function with the filename
    """
    rotate("animal.jpeg")
    return 0


if __name__ == "__main__":
    main()
