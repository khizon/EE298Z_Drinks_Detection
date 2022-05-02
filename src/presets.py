import torch
import torchvision.transforms as T
import numpy as np


class DetectionPresetTrain:
    def __init__(self, *, data_augmentation, hflip_prob=0.5, mean=(123.0, 117.0, 104.0)):
        if data_augmentation == "none":
            self.transforms = T.Compose(
                [
                    T.RandomHorizontalFlip(p=hflip_prob),
                    T.PILToTensor(),
                    T.ConvertImageDtype(torch.float),
                ]
            )

        else:
            raise ValueError(f'Unknown data augmentation policy "{data_augmentation}"')

    def __call__(self, img, target):
        return self.transforms(img)


class DetectionPresetEval:
    def __init__(self):
        self.transforms = T.Compose(
            [
                T.PILToTensor(),
                T.ConvertImageDtype(torch.float),
            ]
        )

    def __call__(self, img, target):
        return self.transforms(img)