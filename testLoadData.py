# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:54:06 2017

@author: 419_2
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from videoto3d import Videoto3D


def main():
    vid3d = Videoto3D(256, 256, 1)
    flist = os.listdir('UCF101')
    #flist.remove('.DS_Store')
    labels = list(set([vid3d.get_UCF_classname(x) for x in flist]))
    
    print (labels)
if __name__ == '__main__':
    main()
