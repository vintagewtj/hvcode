import os
import pydicom
import SimpleITK as sitk
import odl
import numpy as np
import pylab
from torch.autograd._functions import tensor
import astra

from dataset_generator import *

# 调用本地的 dicom file
folder_path = r"../../datasets/projection_data/L067/DICOM-CT-PD_FD"
file_name = "L067_4L_100kv_fulldose1.00003.dcm"
file_path = os.path.join(folder_path, file_name)
ds = pydicom.dcmread(file_path)
# dicom = sitk.ReadImage(file_path)
# print(dicom.GetOrigin())
# data_element = ds.data_element('7031, 1001')
# print(data_element.tag, data_element.VR, data_element.value)
# print(ds.data_element('PatientID'))
# for i in ds.dir()[:]:
#     print(i)
# print(ds.dir('LargestImagePixelValue'))
print(ds.dir('7037, 0010'))
# print(ds.PatientName)
# print(ds)
