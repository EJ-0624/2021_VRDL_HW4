# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 16:26:27 2022

@author: User
"""
import os
root = "C:/Users/User/OneDrive/桌面/NYCU/hw4/SWINIR/datasets"
os.chdir(root)

import numpy as np
import random
import matplotlib.pyplot as plt

train_dir  = "training_hr_images"
train_list = os.listdir(train_dir)

train_Output_Folder = 'train'
if os.path.isdir(train_Output_Folder) is False:
    os.makedirs(train_Output_Folder)
valid_Output_Folder = 'valid' 
if os.path.isdir(valid_Output_Folder) is False:
    os.makedirs(valid_Output_Folder)

for i in train_list:
    image = plt.imread(train_dir + '/' + i)
    prob = random.random()
    if prob >= 0.9:
        plt.imsave(valid_Output_Folder  + '/' + i , image)
    else:
        plt.imsave(train_Output_Folder  + '/' + i , image)
        


#%%
train_file = os.listdir('train')
valid_file = os.listdir('valid')      
def func(pct, number):
    absolute = int(pct/100.*np.sum(number))+1
    return "{:.1f}%\n({:d})".format(pct, absolute)
plt.figure(figsize=(6, 6))
p, l_text, p_text = plt.pie([len(train_file), len(valid_file)], labels=['Train', 'Valid'], 
        autopct=lambda pct: func(pct, [len(train_file), len(valid_file)]), 
        shadow=True, startangle=90)
for t in l_text:
    t.set_size(20)
for t in p_text:
    t.set_size(20)
plt.axis('equal')
plt.show()
    