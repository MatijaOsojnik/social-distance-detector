YOLOV3_LABELS_PATH = 'coco.names'
YOLOV3_CFG_PATH = 'yolov3.cfg'
YOLOV3_WEIGHTS_PATH = 'yolov3.weights'

MIN_CONF = 0.3 # najnižji procent verjetnosti
NMS_THRESH = 0.3 # prag pri uporabi non-maxima suppression


USE_GPU = False # Ne-uporaba NVIDIA CUDA GPU
# define the minimum safe distance (in pixels) that two people can be
# from each other
MIN_DISTANCE = 50 # najmanjša razdlja med dvema osebama v pikslih
