#!/bin/sh
export PYTHONPATH=$PYTHONPATH:/home/vijay/models/research:/home/vijay/models/research/slim
export OBJECT_DETECTION_API_DIR=/home/vijay/models/research/object_detection/
rm -Rf training

#prepare data base after edit flickr_logos_27_dataset, label_map.txt,confg.py
#python3 preproc_annot.py
#prepare tfrecords
#python3 gen_tfrecord.py --train_or_test train --csv_input flickr_logos_27_dataset/flickr_logos_27_dataset_training_set_annotation_cropped.txt --img_dir flickr_logos_27_dataset/flickr_logos_27_dataset_images --output_path train.tfrecord
#python3 gen_tfrecord.py --train_or_test test --csv_input flickr_logos_27_dataset/flickr_logos_27_dataset_test_set_annotation_cropped.txt --img_dir flickr_logos_27_dataset/flickr_logos_27_dataset_images --output_path test.tfrecord
#protoc object_detection/protos/*.proto --python_out=.

OBJECT_DETECTION_API_DIR=/home/vijay/models/research/object_detection/
ln -s ${OBJECT_DETECTION_API_DIR}/ssd_inception_v2_coco_2018_01_28 ssd_inception_v2_coco_2018_01_28
python3 ${OBJECT_DETECTION_API_DIR}/legacy/train.py --logtostderr --pipeline_config_path=ssd_inception_v2_coco.config --train_dir=training
