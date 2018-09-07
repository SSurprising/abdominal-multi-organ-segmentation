import os 
min = 1.0000
loss = 0
path ='/raid/zhangjiaming/Model/abdominal-multi-organ-segmentation/module/'
if not os.path.exists(path):
    print('No such  path')
files = os.listdir(path)
filename = files[0]

for file in files:
    loss = float(file[-9:-4])
    if loss < min:
        min = loss
        filename = file
print('min_mean_loss = ', min)
print('the best module is ', filename)
