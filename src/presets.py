import torch
import transforms as T
import albumentations as A
from albumentations.pytorch import ToTensorV2 as ToTensorV2
import numpy as np


class DetectionPresetTrain:
    def __init__(self, *, data_augmentation, hflip_prob=0.5, mean=(123.0, 117.0, 104.0)):
        if data_augmentation == "hflip":
            self.transforms = A.Compose(
                [
                    A.HorizontalFlip(p=hflip_prob),
                    A.ToFloat(),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'])
            )

        elif data_augmentation == "none":
            self.transforms = A.Compose(
                [
                    A.ToFloat(),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'])
            )

        elif data_augmentation == "drinks":
            self.transforms = A.Compose(
                [
                    A.RandomBrightnessContrast(p=hflip_prob),
                    A.ShiftScaleRotate(p=hflip_prob),
                    A.ToFloat(),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'])
            )

        else:
            raise ValueError(f'Unknown data augmentation policy "{data_augmentation}"')

    def __call__(self, img, target):
        transformed = self.transforms(image=np.asarray(img), bboxes=target["boxes"].numpy(), class_labels=target["labels"].numpy())
        img = transformed["image"]
        target["boxes"] = torch.as_tensor(transformed["bboxes"], dtype=torch.int64)
        target["labels"] = torch.as_tensor(transformed["class_labels"], dtype=torch.int64)

        return img, target


class DetectionPresetEval:
    def __init__(self):
        self.transforms = A.Compose(
                [
                    A.ToFloat(),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'])
            )

    def __call__(self, img, target):
        transformed = self.transforms(image=np.asarray(img), bboxes=target["boxes"].numpy(), class_labels=target["labels"].numpy())
        img = transformed["image"]
        target["boxes"] = torch.as_tensor(transformed["bboxes"], dtype=torch.int64)
        target["labels"] = torch.as_tensor(transformed["class_labels"], dtype=torch.int64)

        return img, target