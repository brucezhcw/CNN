import os, re
import matplotlib.pyplot as plt
from datatools import loadFromH5

def findStep(modelpath):
    if not os.path.exists(modelpath) or len(os.listdir(modelpath)) == 0:
        print('model path not exist, train with initial point')
        return 0
    else:
        l = os.listdir(modelpath)
        step = 0
        match = re.compile(r'ckpt-(\d*)')
        for name in l:
            result = match.findall(name)
            if not len(result) == 0:
                step = max(step, int(result[0]))
        return step

def drawResult(img, stage):
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(img, cmap=plt.cm.gray)
    plt.subplot(2,6,4)
    plt.imshow(stage[:,:,0])
    plt.subplot(2,6,5)
    plt.imshow(stage[:,:,1])
    plt.subplot(2,6,6)
    plt.imshow(stage[:,:,2])
    plt.subplot(2,6,10)
    plt.imshow(stage[:,:,3])
    plt.subplot(2,6,11)
    plt.imshow(stage[:,:,4])
    plt.subplot(2,6,12)
    plt.imshow(stage[:,:,5]) 

def drawMerit(filename = 'merit.h5'):
    step, loss, acc = loadFromH5(filename, ['step', 'loss', 'acc'])
    plt.figure()
    for i in range(3):
        plt.plot(step, loss[:,i])
    plt.figure()
    for j in range(6):
        plt.subplot(2, 3, j + 1)
        for i in range(3):
            plt.plot(step, acc[:,i*3+j])
    plt.show()