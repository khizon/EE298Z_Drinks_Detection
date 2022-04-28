import torch
import transforms as T
import albumentations as A
from albumentations.pytorch import ToTensorV2 as ToTensorV2


class DetectionPresetTrain:
    def __init__(self, *, data_augmentation, hflip_prob=0.5, mean=(123.0, 117.0, 104.0)):
        if data_augmentation == "hflip":
            self.transforms = T.Compose(
                [
                    T.RandomHorizontalFlip(p=hflip_prob),
                    T.PILToTensor(),
                    T.ConvertImageDtype(torch.float),
                ]
            )

        elif data_augmentation == "none":
            self.transforms = T.Compose(
                [
                    T.PILToTensor(),
                    T.ConvertImageDtype(torch.float),
                ]
            )

        elif data_augmentation == "drinks":
            self.transforms = A.Compose(
                [
                    ToTensorV2(),
                ]
            )

        else:
            raise ValueError(f'Unknown data augmentation policy "{data_augmentation}"')

    def __call__(self, img, target):
        transformed = self.transforms(image=np.asarray(img), bboxes=target["boxes"].numpy(), class_labels=target["labels"].numpy())
        img = transformed["image"]
        target["boxes"] = torch.as_tensor(transformed["bboxes"], dtype=torch.uint8)
        target["labels"] = torch.as_tensor(transformed["class_labels"], dtype=torch.uint8)

        return img, target


class DetectionPresetEval:
    def __init__(self):
        data_augmentation == "drinks":
            self.transforms = A.Compose(
                [
                    ToTensorV2(),
                ]
            )

    def __call__(self, img, target):
        transformed = self.transforms(image=np.asarray(img), bboxes=target["boxes"].numpy(), class_labels=target["labels"].numpy())
        img = transformed["image"]
        target["boxes"] = torch.as_tensor(transformed["bboxes"], dtype=torch.uint8)
        target["labels"] = torch.as_tensor(transformed["class_labels"], dtype=torch.uint8)

        return img, target