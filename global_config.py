# If using batch size = 1, ONE_IMAGE_SIZE can be false
# Otherwise a batch size > 1 requires images of the same size and ONE_IMAGE_SIZE must be true
ONE_IMAGE_SIZE = False
# Most of the AcTiV labeled samples are 720x576. Note that AlJazeeraHD is not
INPUT_WIDTH = 720
INPUT_HEIGHT = 576
# Color might not a meaningful feature for Arabic detection
USE_GRAYSCALE = False