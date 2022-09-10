'''
This application can be used to backup data in a directory to an external usb drive

@author Tharuka Pavith
'''

import os, shutil

def copy_with_meta_data(src: str, dst: str):
    '''
    Copies a directory including file meta-data to a destination directory
    '''
    shutil.copytree(src, dst, dirs_exist_ok=True)

def recursive_copy(src, dst):
    l = os.listdir(src)
    print(l)
    for i in l:
        if (os.path.isdir(i)): #This is a directory
            recursive_copy(os.path.join(src,i), os.path.join(dst, i))
            #print(f'Directory: {i}')
        else: #this is a directory
            shutil.copyfile(os.path.join(src,i), os.path.join(dst,i), follow_symlinks=False)
            #print(f'File: {i}')


if __name__ == '__main__':
    src = 'original/'
    dst = 'E:\\Backup_Files'
    if not os.path.isdir(dst):
        os.mkdir(dst)
    
    copy_with_meta_data(src, dst)
   
    
