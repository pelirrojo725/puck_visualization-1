#!/bin/bash
if [ -d /Users/samuel/Desktop/Projects/puck_visualization ]; then
    export PUCK_ROOT=/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/var/model_data/Temp
fi

base_image=${PUCK_ROOT}/image_for_corrections
fname=$1
fname=${fname%%.*}
fbase=${fname}_position

tmp_dir=$PWD/${USER}_puck_visualization_$$
mkdir $tmp_dir

printf "Processing image: ${1}\n"
printf "Files in: ${tmp_dir}\n"

DEFAULT_ROI_WIDTH=$((143))
DEFAULT_ROI_HIEGHT=$((141))

#Cropping down the images for each position of a pin on the puck
convert $1 ${tmp_dir}/${fname}.jpg
# python3 ${PUCK_ROOT}/clahe_image.py ${tmp_dir}/${fname}.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+415+456 ${tmp_dir}/${fbase}_1.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+510+325 ${tmp_dir}/${fbase}_2.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+667+372 ${tmp_dir}/${fbase}_3.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+667+534 ${tmp_dir}/${fbase}_4.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+514+589 ${tmp_dir}/${fbase}_5.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+255+458 ${tmp_dir}/${fbase}_6.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+301+296 ${tmp_dir}/${fbase}_7.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+427+182 ${tmp_dir}/${fbase}_8.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+594+157 ${tmp_dir}/${fbase}_9.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+748+225 ${tmp_dir}/${fbase}_10.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+844+366 ${tmp_dir}/${fbase}_11.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+844+536 ${tmp_dir}/${fbase}_12.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+752+683 ${tmp_dir}/${fbase}_13.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+601+751 ${tmp_dir}/${fbase}_14.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+433+732 ${tmp_dir}/${fbase}_15.jpg
convert ${tmp_dir}/${fname}.jpg -crop ${DEFAULT_ROI_WIDTH}x${DEFAULT_ROI_HIEGHT}+303+621 ${tmp_dir}/${fbase}_16.jpg

for i in {1..16}; do
    # python3 ${PUCK_ROOT}/flat_field_correction.py ${tmp_dir}/${fbase}_${i}.jpg ${base_image}/position_${i}.jpg
    # python3 ${PUCK_ROOT}/thresholding_image.py ${tmp_dir}/${fbase}_${i}.jpg
    cp ${tmp_dir}/${fbase}_${i}.jpg /home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/var/model_data/cropped_unsorted
done
