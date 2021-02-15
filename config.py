import os

TRAIN_DIR = 'flickr_logos_27_dataset'
IMAGES_DIR = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_images')
CROPPED_IMAGES_DIR = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_images_cropped')
ANNOT_FILE = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_training_set_annotation.txt')
CROPPED_ANNOT_FILE = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_training_set_annotation_cropped.txt')
CROPPED_ANNOT_FILE_TEST = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_test_set_annotation_cropped.txt')

CLASS_NAMES = ['liveu' ]
CLASS_NAMES_FILE = os.path.join(TRAIN_DIR, 'flickr_logos_27_dataset_class_names.txt')
