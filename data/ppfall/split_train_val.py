# 划分VOC数据集
import os
import random

#datasets_path = r'D:\test_file\VOCdevkit\VOC2007/'  # 数据集路径
datasets_path = r'C:\Users\hp\Desktop\qcs\yolov5-master\data\ppfall/'  # 数据集路径

trainval_percent = 0.8 #训练和验证集所占比例，剩下的就是测试集的比例
train_percent = 0.7 #训练集所占比例
xml_path = datasets_path + 'Annotations'
txtsavepath = datasets_path + 'ImageSets/Main'
total_xml = os.listdir(xml_path)

num = len(total_xml)
list1 = range(num)
tmtp = int(num * trainval_percent)
trp = int(tmtp * train_percent)
trainval = random.sample(list1, tmtp)
train = random.sample(trainval, trp)

with open(datasets_path + 'ImageSets/Main/trainval.txt', 'w') as ftrainval, \
        open(datasets_path + 'ImageSets/Main/test.txt', 'w') as ftest, \
        open(datasets_path + 'ImageSets/Main/train.txt', 'w') as ftrain, \
        open(datasets_path + 'ImageSets/Main/val.txt', 'w') as fval:

    for i in list1:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)
