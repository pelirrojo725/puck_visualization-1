#!/bin/bash
if [ -d /home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/bin ]; then
	export PUCK_ROOT=/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/bin
fi

train_dir=${PUCK_ROOT}/train_model

fname=$1
fname=${fname%%.*}
fbase=${fname}_position

if [ "${1}xx" == "--helpxx" ]; then
	echo "The image of the puck is input as an argument and "
	echo "each pin is tested to "
	exit
fi

tmp_dir=$PWD/${USER}_puck_visualization_$$
mkdir $tmp_dir

printf "Processing image: ${1}\n"
printf "Files in: ${tmp_dir}\n"

#Cropping down the images for each position of a pin on the puck
python3.8 ${PUCK_ROOT}/crop_images.py $1 $tmp_dir $fbase

echo Testing Positions:
python3.8 ${PUCK_ROOT}/predict_position.py ${train_dir} ${tmp_dir} $1

# for i in {1..16}; do
# 	python3 ${PUCK_ROOT}/flat_field_correction.py ${tmp_dir}/${fbase}_${i}.jpg ${base_image}/position_${i}.jpg
# 	python3 ${PUCK_ROOT}/thresholding_image.py ${tmp_dir}/${fbase}_${i}.jpg
# done

# for i in {1..16}; do
# 	printf "Image ${1}\n" >>${tmp_dir}/${USER}_output_$$.txt
# 	printf "${tmp_dir}\n" >>${tmp_dir}/${USER}_output_$$.txt
# 	single_process_white_pixels=$(convert ${tmp_dir}/${fbase}_${i}.jpg -format "%[fx:w*h*mean]" info:)
# 	single_process_white_pixels=${single_process_white_pixels%.*}
# 	single_process_black_pixels=$((20163 - ${single_process_white_pixels}))
# 	printf "\nBlack pixels: ${single_process_black_pixels}\n\n" >>${tmp_dir}/${USER}_output_$$.txt
# done

#open ${tmp_dir}/${fbase}_*.jpg
#open ${tmp_dir}/${USER}_output_$$.txt
