#cd /data1/models
#cp vgg19-dcbb9e9d.pth /root/.cache/torch/hub/checkpoints/vgg19-dcbb9e9d.pth
cd /data1/projects/new_experiments/ana100_4_3
python  train.py > /data1/projects/new_experiments/ana100_4_3/run.log
