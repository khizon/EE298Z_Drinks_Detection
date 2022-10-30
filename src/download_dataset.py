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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar_ref, os.path.join(data))
        
    os.rename(os.path.join(data, 'drinks'), os.path.join(data, 'imgs'))