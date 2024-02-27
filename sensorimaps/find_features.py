import cv2  # type: ignore


def map_contours(img):
    """find contours within a map image.
    The image is converted to grayscale, then binarized.
    Contours are then identified using the external method so any small holes or missed regions are ignored.

    Parameters
    ----------
    img : array-like
        image array in shape (height, width, color_channels)

    Returns
    -------
    list of contour data
        each list item is a contour array
    """
    # Convert to grayscale and binarize
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(img_gray, 150, 1, cv2.THRESH_BINARY_INV)

    # Identify contours (external only)
    contours, _ = cv2.findContours(
        img_bin, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE
    )
    return contours, img_bin
