import os

root = '/data1/datasets/120_angles_in360_clean/train_data'
target_path = os.path.join(root, 'targets')
target_list = os.listdir(target_path)
target_list.sort(key=lambda x:int(x.split('et')[1].split('.')[0]))

sinogram_path = os.path.join(root, 'sinograms')
sinogram_list = os.listdir(sinogram_path)
sinogram_list.sort(key=lambda x:int(x.split('am')[1].split('.')[0]))
for i in range(len(target_list)):
    oldname = target_path + os.sep + target_list[i]
    newname = target_path + os.sep + 'target{0}.bmp'.format(i)
    os.rename(oldname, newname)

for i in range(len(sinogram_list)):
    oldname = sinogram_path + os.sep + sinogram_list[i]
    newname = sinogram_path + os.sep + 'sinogram{0}.bmp'.format(i)
    os.rename(oldname, newname)
