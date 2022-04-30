import os

if __name__ == '__main__':
    command = f'pip install -r requirements.txt'
    os.system(command)

    command = f'python src/download_dataset.py'
    os.system(command)

    command = f'torchrun --nproc_per_node=1 src/train.py\
                --dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_fpn\
                --test-only --resume https://github.com/khizon/EE298Z_Drinks_Detection/releases/download/v0.0/checkpoint.pth\
                --data-augmentation none > logs.txt'
    
    os.system('clear')
    os.system(command)