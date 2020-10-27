#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 此代码和data文件夹同目录
# 将一个文件夹下图片按比例分在两个文件夹下，比例改0.8这个值即可
import os
import random
import shutil
from shutil import copy2
trainfiles = os.listdir('train_images/')#（图片文件夹）
num_train = len(trainfiles)
print( "num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)
num = 0
trainDir = 'data/train_images/'#（将图片文件夹中的8/10份放在这个文件夹下）
validDir = 'data/val_images/'#（将图片文件夹中的2/10份放在这个文件夹下）
for i in index_list:
    fileName = os.path.join('train_images/', trainfiles[i])
    if num < num_train*0.8:
        print(str(fileName))
        copy2(fileName, trainDir)
    else:
        copy2(fileName, validDir)
    num += 1