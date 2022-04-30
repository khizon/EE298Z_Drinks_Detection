# EE298Z_Drinks_Detection

FastRCNN is a blah blah blah

[Original Paper]()

This repository used code from the following repositories:
* [ViTSTR](https://github.com/roatienza/deep-text-recognition-benchmark)
* [PyTorch Vision Reference](https://github.com/pytorch/vision/tree/main/references/detection)

## Folder structure
Please use `data/annotations/labels_***.csv` to train and test the model.

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
    |   | /train.py
    |   | ...
    | /artifacts
    | checkpoint.pth
    | logs.txt
```

## Dependencies


`pip install -r requirements.txt`


## Usage

### Downloading the dataset
You can download the augmented annotations from Google Drive using the following command:

`python src/download_dataset.py`

### Inference
Test the released model on a sample image.

### Testing
Test the released model on the test set.


```
torchrun --nproc_per_node=1 src/train.py\
--dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_fpn\
--test-only --resume https://github.com/khizon/EE298Z_Drinks_Detection/releases/download/v0.0/checkpoint.pth\
--data-augmentation none > logs.txt
```

The model will be downloaded at `data/checkpoint.pth` and the results will be written to `logs.txt`.

### Training

```
torchrun --nproc_per_node=1 src/train.py\
--dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_fpn --epochs 26\
--lr-steps 16 22 --aspect-ratio-group-factor 3\
--output-dir artifacts/temp --data-augmentation none --pretrained > logs.txt
```


You must modify the following flags:

`--data-path=<root_directory_of_dataset>`

`--nproc_per_node=<number_of_gpus_available>`

For debugging purposes, use subset of dataset:

`--dataset drinks_subset`

To enable data augmentation:

`--data-augmentation drinks`


