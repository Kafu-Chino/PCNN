#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2020/3/22 23:04
# Author : Hu
# File : filternyt_data.py

from torch.utils import data
import os

class FilterNyt(data.Dataset):
    def __init__(self, data_path, train=True, test=False):
        if train:
            path = os.path.join(data_path, 'train/')
            print('开始加载训练数据集')
        else:
            path = os.path.join(data_path, 'train/')
            print('开始加载测试数据集')

