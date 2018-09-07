import os
import random

import torch
import torch.nn.functional as F
from torch.autograd import Variable
from torch.utils.data import Dataset as dataset

import SimpleITK as sitk
import scipy.ndimage as ndimage

ct_dir = '/raid/zhangjiaming/Model/abdominal-multi-organ-segmentation/3D/test/CT/'
seg_dir = '/raid/zhangjiaming/Model/abdominal-multi-organ-segmentation/3D/test/GT/'

ct_list = os.listdir(ct_dir)
seg_list = list(map(lambda x: x.replace('img', 'label'), ct_list))

for i in range(len(ct_list)):
    ct_path = ct_dir + str(ct_list[i])
    seg_path = seg_dir + str(seg_list[i])

    ct = sitk.ReadImage(ct_path, sitk.sitkInt16)
    seg = sitk.ReadImage(seg_path, sitk.sitkUInt8)

    ct_array = sitk.GetArrayFromImage(ct)
    seg_array = sitk.GetArrayFromImage(seg)
    ct_array = torch.FloatTensor(ct_array).unsqueeze(0)
    seg_array = torch.FloatTensor(seg_array)

    print('ct_array.size = ', ct_array.size())
    print('seg_array.size = ', seg_array.size())
