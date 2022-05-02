import os

if __name__ == '__main__':
    
    command = f'pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113'
    os.system(command)
    command = f'pip install -r requirements.txt'
    os.system(command)

    if not os.path.exists('data/imgs/'):
        command = f'python src/download_dataset.py'
        os.system(command)

    command = f'torchrun --nproc_per_node=1 src/train.py\
                --dataset drinks --data-path data --model fasterrcnn_mobilenet_v3_large_fpn\
                --test-only --resume https://github.com/khizon/EE298Z_Drinks_Detection/releases/download/v1.0/fasterrcnn_mobilenet_v3_large_fpn_none.pth'
    
    os.system('clear')
    os.system(command)