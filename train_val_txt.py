#  此代码和data文件夹同目录
#  產生data中train_images及val_images資料夾中的文件清單txt
import glob

path = 'data/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.jpg'):
            tf.write(jpg_file + '\n')

generate_train_and_val(path + 'train_images/', path + 'train.txt')
generate_train_and_val(path + 'val_images/', path + 'val.txt')