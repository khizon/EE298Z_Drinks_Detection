import os

def get_args_parser(add_help=True):
    import argparse
    parser = argparse.ArgumentParser(description="PyTorch Detection Training", add_help=add_help)
    
    parser.add_argument(
        "--test-only",
        dest="test_only",
        help="Only test the model",
        action="store_true",
    )
    
    parser.add_argument(
        "--debug",
        dest="debug",
        help="Subset only",
        action="store_true",
    )
    
    return parser

if __name__ == '__main__':
    args = get_args_parser().parse_args()
    
    if args.debug:
        dataset = 'drinks_subset'
        project = 'my-test-project'
    else:
        dataset = 'drinks'
        project = 'EE298Z_Drinks_Detection'
        
    if args.test_only:
        command = f'torchrun --nproc_per_node=1 src/train.py\
                --dataset {dataset} --data-path data --model fasterrcnn_mobilenet_v3_large_320_fpn\
                --test-only --resume artifacts/temp/checkpoint.pth  --data-augmentation none --project {project} > logs.txt'
    else:
        command = f'torchrun --nproc_per_node=1 src/train.py\
            --dataset {dataset} --data-path data --model fasterrcnn_mobilenet_v3_large_320_fpn --epochs 26\
            --lr-steps 16 22 --aspect-ratio-group-factor 3\
            --output-dir artifacts/temp --data-augmentation none --pretrained --project {project} > logs.txt'
    
    
    os.system('clear')
    os.system(command)