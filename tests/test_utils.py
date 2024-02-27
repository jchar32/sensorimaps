import os
from sensorimaps.utils import load_img
import pytest


@pytest.fixture
def img_path():
    img_path = os.path.abspath("./sample_data/img_1.png")
    return img_path


def test_load_img(img_path):
    # img_path = os.path.abspath("./sample_data/img_1.png")
    print(img_path)
    img = load_img(img_path)
    assert img is not None, "file could not be read, check with os.path.exists()"


def test_load_img_with_invalid_path(img_path):
    # img_path = os.path.abspath("../sample_data/non_existent.png")
    img = load_img(os.path.join(img_path, "non_existent.png"))
    assert img is None, "file should not be read, as it does not exist"
