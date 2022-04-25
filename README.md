# EE298Z_Drinks_Detection

This folder contains modified scripts for training object detection models. The original code are available at [] and []

## Folder structure

```
EE298Z_Drinks_Detection
    | /data
    |   | /annotations
    |   |   | labels_test_subset.csv
    |   |   | labels_train_subset.csv
    |   |   | labels_test.csv
    |   |   | labels_train.csv
    |   | /imgs
    |       | 0000000.jpg
    |       | 0000001.jpg
    |       | ...
    | /src
    | /artifacts
```

## Dependencies

To execute the example commands below you must install the following:

```
pytorch & torchvision
gdown (to download the dataset from gdrive)
cython
pycocotools
matplotlib
wandb (to log training progress)
```
Alternatively run:
`pip install -r requirements.txt`


## Usage
Execute the torchrun command below to train the model. Alternatively, you can edit  `src/runner.py` and run it using the command `python src/runner.py`

You must modify the following flags:

`--data-path=/path/to/coco/dataset`

`--nproc_per_node=<number_of_gpus_available>`

All models have been trained on 1x T4 GPUs. 

### Drinks Detection
For debugging purposes, use subset of dataset:

`--dataset drinks_subset`

Training loss and live logs can be viewed in Weights and Biases. Outputs of the evaluation can be found in `artifacts/logs.txt ` and the model will be saved in `--output-dir`

```
torchrun --nproc_per_node=1 src/train.py\
    --dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_320_fpn --epochs 26\
    --lr-steps 16 22 --aspect-ratio-group-factor 3 --weights-backbone MobileNet_V3_Large_Weights.IMAGENET1K_V1\
    --output-dir artifacts --data-augmentation none > artifacts/logs.txt
```