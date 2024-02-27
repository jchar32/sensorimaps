import os
import cv2  # type: ignore


def find_files(full_path, image_type=".png"):
    """Based on full path name, finds all files with the specified image type file extension

    Parameters
    ----------
    full_path : path-like
        absolute path to the directory containing the image files
    image_type : str, optional
        file extension for image files to be processes, by default ".png"

    Returns
    -------
    array-like
        image_file_names: list of file names from the specified directory with the specified image type file extension
    """
    image_file_names = [
        fname for fname in os.listdir(full_path) if fname.endswith(image_type)
    ]
    return image_file_names


def load_img(img_path):
    """Loads an image from a file path

    Parameters
    ----------
    img_path : path-like
        absolute path to the image file

    Returns
    -------
    array-like
        img: image array
    """
    img = cv2.imread(img_path)
    return img
