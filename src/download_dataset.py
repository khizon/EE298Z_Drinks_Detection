import os
import zipfile
import tarfile
import gdown

if __name__ == '__main__':
    # Dataset
    url = 'https://drive.google.com/drive/folders/1mN0v95iEKl0V7myAisuNjRaHIdEr_55O?usp=sharing'
    data = './data/'
    
    if not os.path.exists(data):
        os.makedirs(data)
    
    os.system(f'clear')
    
    if not os.path.exists(os.path.join('./', 'drinks.tar.gz')):
        # os.system(f'gdown --folder {url} -O {data}')
        gdown.download_folder(url, use_cookies=False)
        
    if not os.path.exists(os.path.join('./', 'drinks.tar.gz')):
        print('Download failed')
    
    with zipfile.ZipFile(os.path.join('./', 'annotations.zip'), 'r') as zip_ref:
        zip_ref.extractall(os.path.join(data))
    
    with tarfile.open(os.path.join('./', 'drinks.tar.gz'), 'r') as tar_ref:
        tar_ref.extractall(os.path.join(data))
        
    os.rename(os.path.join(data, 'drinks'), os.path.join(data, 'imgs'))