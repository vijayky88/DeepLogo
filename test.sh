#!/bin/sh
export PYTHONPATH=$PYTHONPATH:/home/vijay/models/research:/home/vijay/models/research/slim
export OBJECT_DETECTION_API_DIR=/home/vijay/models/research/object_detection/
STEPS=$1
rm -Rf logos_inference_graph 
python3 ${OBJECT_DETECTION_API_DIR}/export_inference_graph.py --input_type=image_tensor --pipeline_config_path=ssd_inception_v2_coco.config --trained_checkpoint_prefix=training/model.ckpt-${STEPS} --output_directory=logos_inference_graph

rm -Rf detect_results
python3 logo_detection.py --model_name logos_inference_graph/ --label_map flickr_logos_27_label_map.pbtxt --test_annot_text flickr_logos_27_dataset/flickr_logos_27_dataset_test_set_annotation_cropped.txt --test_image_dir flickr_logos_27_dataset/flickr_logos_27_dataset_images --output_dir detect_results

#please chnage Cast to Cast_1 in ssd_support_api_v.1.14
#https://docs.openvinotoolkit.org/2019_R3.1/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html#freeze-the-tensorflow-model
cd logos_inference_graph/
python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb -b 1 --tensorflow_object_detection_api_pipeline_config  pipeline.config  --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_support_api_v1.14.json
cd ..

echo "Done"
