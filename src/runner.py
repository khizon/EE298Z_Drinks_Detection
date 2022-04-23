import os

if __name__ == '__main__':
    command = f'torchrun --nproc_per_node=1 src/train.py\
    --dataset drinks_subset --data-path data --model fasterrcnn_mobilenet_v3_large_320_fpn --epochs 2\
    --lr-steps 16 22 --aspect-ratio-group-factor 3 --weights-backbone MobileNet_V3_Large_Weights.IMAGENET1K_V1\
    --output-dir artifacts/temp --data-augmentation none'
    
    os.system(command)