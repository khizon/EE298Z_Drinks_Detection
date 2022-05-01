# EE298Z_Drinks_Detection
Submitted by **Kiel Hizon** 2013-17614

This project fine-tuned the [Faster RCNN](https://arxiv.org/abs/1506.01497) [MobileNet V3 Large FPN](https://pytorch.org/vision/stable/generated/torchvision.models.detection.fasterrcnn_mobilenet_v3_large_fpn.html) which was originally trained on the COCO 2017 dataset to detect 3 kinds of drinks (Coca-cola Original in can, Pineapple Juice in can, and Summit bottled water). Albumentations was used to add random shift, scale, rotate, brightness, and contrast changes to the training data. The models were trained on a Google Cloud virtual environment with 1x NVidia Tesla T4 GPU. **The training took about 30 minutes for 26 epochs.**

This repository used code from the following repositories:
* [ViTSTR](https://github.com/roatienza/deep-text-recognition-benchmark)
* [PyTorch Vision Reference](https://github.com/pytorch/vision/tree/main/references/detection)

## Folder structure
For EE298Z Checking: run `python train.py` or `python test.py` it will install the required dependencies, download the dataset, and released model (no augmentation).

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
    | train.py
    | test.py
```

## Dependencies


`pip install -r requirements.txt`


## Usage

### Downloading the dataset
You can download the augmented annotations from Google Drive using the following command:

`python src/download_dataset.py`


### Testing
Test the released model on the test set.


```
torchrun --nproc_per_node=1 src/train.py\
--dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_fpn\
--test-only --resume https://github.com/khizon/EE298Z_Drinks_Detection/releases/download/v1.0/fasterrcnn_mobilenet_v3_large_fpn_none.pth > logs.txt
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

## Results
AP = Average Precision, AR = Average Recall, IoU = Intersection over Union

| Metric | IoU            | Area | maxDets | Base  | Augmented |
| ------ | -------------- | ---- | ------- | ----- | --------- |
| AP     | @ IoU=0.5:0.95 | all  | 100     | 0.866 | 0.848     |
| AP     | @ IoU=0.50     | all  | 100     | 0.980 | 0.980     |
| AP     | @ IoU=0.75     | all  | 100     | 0.966 | 0.953     |
| AR     | @ IoU=0.5:0.95 | all  | 100     | 0.822 | 0.815     |
| AR     | @ IoU=0.50     | all  | 100     | 0.894 | 0.885     |
| AR     | @ IoU=0.75     | all  | 100     | 0.894 | 0.885     |

Base model has better precision and recall compared to the augmented. This may be due to the **spatial modifications can sometimes remove all objects of interest** from the picture. I am not sure that I handled that scenario properly.

[Demo Video (Input webcam is 1080p)](https://youtu.be/vjiDqnxS5P4)
