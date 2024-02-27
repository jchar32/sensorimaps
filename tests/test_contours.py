from sensorimaps import find_features, utils
import pytest


@pytest.fixture
def image_data():
    # Load the image
    img_path = "sample_data/img_1.png"
    img = utils.load_img(img_path)
    return img


def test_find(image_data):
    # Call the find function
    contours, img_bin = find_features.map_contours(image_data)

    # Assert that the returned contours are not empty
    assert len(contours) == 1

    # Assert that the shape of the binarized image should be 2D
    assert img_bin.ndim == 2

    # Assert that the binarized image contains only 0s and 1s
    assert set(img_bin.flatten()) == {0, 1}
