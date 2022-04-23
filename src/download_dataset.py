import os

if __name__ == '__main__':
    # Dataset
    url = 'https://drive.google.com/drive/folders/1mN0v95iEKl0V7myAisuNjRaHIdEr_55O?usp=sharing'
    data = 'data/'
    
    os.system(f'gdown --folder {url} -O {data}')
    
    os.system(f'tar -xzf data/drinks.tar.gz -C data/')
    os.system(f'mv data/drinks data/imgs')