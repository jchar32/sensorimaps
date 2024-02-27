# %%
from sensorimaps import find_features, utils


img = utils.load_img("../sample_data/img_1.png")
contours, img_bin = find_features.map_contours(img)
